#include <iostream>
#include <array>
#include <memory>

template<std::size_t N>
constexpr auto encrypt(const char (&str)[N], char key) {
    std::array<int, N> crypted{};
    for (std::size_t i = 0; i < N; i++) {
        crypted[i] = static_cast<int>(str[i]) ^ ((i % 3) + key);
    }
    return crypted;
}

const char key = 0x69;
constexpr auto flag = encrypt("YBN24{P4TCH1NG_D33Z_NU75_H33_H33}", key);

void win() {
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x00, 0x90, 0x00, 0x90\n"\
                "1:" : : : "rax");
    std::unique_ptr<char[]> decrypted(new char[flag.size()]);
    for (std::size_t i = 0; i < flag.size(); i++) {
        volatile int dummy = i * 42;

        decrypted[i] = static_cast<char>((flag[i]) ^ ((i % 3) + (key)));
    }

    std::cout << "flag: " << decrypted.get() << std::endl;
    int a;
    std::cin >> a;
}

int login() {
    std::string password;

    std::cout << "Enter password: ";
    std::cin >> password;

    if (password.length() > 16) {
        password = password.substr(0, 16);
    }
    if (password == "how to get right password!?!?!?!?!") {
        printf("\n\n%s\n", "how o.O");
        win();

        return 0;
    } else {
        printf("%s\n", "can't crack me :p");
        return 1;
    }
}

int main() {
    login();

    return 0;
}