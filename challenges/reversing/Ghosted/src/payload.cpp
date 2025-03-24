// couldn't get Donut to work with this :skull:
// g++ -o payload.exe payload.cpp -lws2_32
// donut --input:payload.exe -k:1 -z:2 -e:1 -f:3

#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <random>

#pragma comment(lib, "ws2_32.lib")

char encrypted_flag[] = {
        0x51, 0x4a, 0x46, 0x3a, 0x3c, 0x73, 0x4c, 0x3b,
        0x3b, 0x52, 0x57, 0x46, 0x5d, 0x45, 0x4a, 0x3b,
        0x5a, 0x5b, 0x57, 0x4c, 0x38, 0x46, 0x5c, 0x57,
        0x4b, 0x40, 0x3c, 0x46, 0x4f, 0x3b, 0x57, 0x4d,
        0x39, 0x5c, 0x40, 0x3b, 0x5a, 0x75
};

DWORD WINAPI cleanup_thread(LPVOID timer) {
    WaitForSingleObject((HANDLE)timer, INFINITE);
    ExitProcess(0);
    return 0;
}

void send_message(SOCKET client, const char* msg) {
    send(client, msg, lstrlenA(msg), 0);
    if (!strchr(msg, '\n')) send(client, "\n", 1, 0);
}

int get_client_guess(SOCKET client, char* buffer, size_t buffer_size) {
    memset(buffer, 0, buffer_size);
    size_t pos = 0;
    while (pos < buffer_size - 1) {
        char c;
        if (recv(client, &c, 1, 0) <= 0) return -1;
        if (c == '\n' || c == '\r') {
            if (pos > 0) break;
            continue;
        }
        buffer[pos++] = c;
    }
    return atoi(buffer);
}

void play_game(SOCKET client) {
    DWORD timeout = 10000;
    setsockopt(client, SOL_SOCKET, SO_RCVTIMEO, (char*)&timeout, sizeof(timeout));

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 1000000);

    send_message(client, "beep boop\nguess 1000 numbers back to back for the flag\nconstraints: \n1 >= n >= 1000000\ntimeout = 10s\n\nsince im so generous: std::random_device rd; std::mt19937 gen(rd()); std::uniform_int_distribution<> dis(1, 1000000);\n\n");

    char buffer[1024];
    int correct_guesses = 0;
    int res[1000] = {0};

    while (correct_guesses < 1000) {
        int target = dis(gen);
        send_message(client, "number: ");

        int guess = get_client_guess(client, buffer, sizeof(buffer));
        if (guess == -1) {
            send_message(client, "womp womp");
            return;
        }

        if (guess == target) {
            res[correct_guesses] = guess & 0xFF;  // Save every guess
            correct_guesses++;
            char progress[64];
            wsprintfA(progress, "good. %d/1000", correct_guesses);
            send_message(client, progress);
        } else {
            char wrong[64];
            wsprintfA(wrong, "noob", target);
            send_message(client, wrong);
            send_message(client, "gg");
            return;
        }
    }

    char flag[sizeof(encrypted_flag)];
    memcpy(flag, encrypted_flag, sizeof(encrypted_flag));
    for(int i = 0; i < correct_guesses; i++) {
        for(size_t j = 0; j < sizeof(flag); j++) {
            flag[j] ^= res[i];
        }
    }

    char congrats[256];
    wsprintfA(congrats, "enjoy flag: %s", flag);
    send_message(client, congrats);
}

extern "C" __declspec(dllexport)
DWORD WINAPI ServerEntry(LPVOID lpParam) {
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);

    HANDLE cleanup_timer = CreateWaitableTimer(NULL, TRUE, NULL);
    LARGE_INTEGER due_time;
    due_time.QuadPart = -500000000LL * 60 * 5;
    SetWaitableTimer(cleanup_timer, &due_time, 0, NULL, NULL, FALSE);
    CreateThread(NULL, 0, cleanup_thread, cleanup_timer, 0, NULL);

    SOCKET server_sock = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in server = {AF_INET, 0, INADDR_ANY};

    bind(server_sock, (struct sockaddr*)&server, sizeof(server));
    listen(server_sock, SOMAXCONN);

    while (true) {
        sockaddr_in client;
        int client_size = sizeof(client);
        SOCKET client_sock = accept(server_sock, (struct sockaddr*)&client, &client_size);
        play_game(client_sock);
        closesocket(client_sock);
    }
}

int main() {
    ServerEntry(NULL);
    return 0;
}