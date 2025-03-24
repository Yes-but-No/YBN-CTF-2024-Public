#include <iostream>
#include <cstring>
#include <random>
#include <thread>
#include <functional>
#include <sys/mman.h>
#include <sys/ptrace.h>
#include "Obfusheader.h"

#define MOD 8


constexpr unsigned char flag_key = 0x69;
constexpr unsigned char debugger_check[] = "\xb8\x65\x00\x00\x00\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x4d\x31\xd2\x0f\x05\x48\x83\xf8\xff\x75\x05\xe9\xec\xff\x7f\x77\xc3";

__attribute__((always_inline)) inline void nothing_sus(size_t size) {
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x00, 0x00, 0x00, 0x00\n"\
                "1:" : : : "rax");


    void *mem = CALL(&mmap, nullptr, size, OBF(PROT_EXEC | PROT_READ | PROT_WRITE), OBF(MAP_PRIVATE | MAP_ANONYMOUS), -1, 0);
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x13, 0x37, 0x69, 0x69\n"\
                "1:" : : : "rax");


    CALL(&memcpy, mem, debugger_check, size);
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x13, 0x33, 0x37, 0x00\n"\
                "1:" : : : "rax");



    ((void (*)())mem)();
    CALL(&munmap, mem, size);
}

constexpr uint64_t constexpr_hash(const unsigned char* data, size_t size) {
    constexpr uint64_t FNV_OFFSET_BASIS = 14695981039346656037ULL;
    constexpr uint64_t FNV_PRIME = 1099511628211ULL;

    uint64_t hash = FNV_OFFSET_BASIS;

    for (size_t i = 0; i < size; ++i) {
        hash ^= static_cast<uint64_t>(data[i]);
        hash *= FNV_PRIME;
    }

    return hash;
}

template<size_t N, size_t K>
constexpr auto enc_flag(const std::array<int, N>& input, const unsigned char (&key)[K]) {
    std::array<int, N> result{};
    uint64_t key_hash = constexpr_hash(key, K);
    for (size_t i = 0; i < N; ++i) {
        result[i] = input[i] ^ ((key_hash >> (MOD * (i % MOD))) & 0xFF);
    }
    return result;
}

template<std::size_t N, std::size_t K>
std::array<int, N> dec_flag(const std::array<int, N>& encrypted_flag, const unsigned char (&key)[K]) {
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0xb8, 0x65, 0x00, 0x69\n"\
                "1:" : : : "rax");
    std::array<int, N> decrypted{};
    asm volatile(\
            "xor %%rax, %%rax\n"\
            "jz 1f\n"\
            ".byte 0xc3, 0xc3, 0xc3, 0xc3\n"\
            "1:" : : : "rax");
    CALL(&nothing_sus, sizeof(debugger_check));
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x42, 0x20, 0x69, 0x90\n"\
                "1:" : : : "rax");
    uint64_t key_hash = constexpr_hash(key, K);
    ofor (size_t i = 0; i < N; ++i) {
        asm volatile("xor %%rax, %%rax\njz 1f\n.byte 0x00, 0x00, 0x00, 0x00\n1:" : : : "rax");
        decrypted[i] = encrypted_flag[i] ^ ((key_hash >> (OBF(MOD) * (i % OBF(MOD)))) & OBF(0xFF));
    }
    oreturn decrypted;
}

template<std::size_t N>
constexpr auto encrypt(const char (&str)[N], char key) {
    std::array<int, N> crypted{};
    for (std::size_t i = 0; i < N; i++) {
        crypted[i] = static_cast<int>(str[i]) ^ ((i % MOD) + key);
    }
    return crypted;
}

template<std::size_t N>
__attribute__((always_inline)) std::string decrypt(const std::array<int, N> &crypted, char key) {
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0xb8, 0x65, 0x00, 0x69\n"\
                "1:" : : : "rax");
    std::string decrypted(N, OBF('\0'));
    asm volatile(\
            "xor %%rax, %%rax\n"\
            "jz 1f\n"\
            ".byte 0xc3, 0xc3, 0xc3, 0xc3\n"\
            "1:" : : : "rax");
    CALL(&nothing_sus, sizeof(debugger_check));
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x42, 0x20, 0x69, 0x90\n"\
                "1:" : : : "rax");
    ofor (std::size_t i = 0; i < N; i++) {
        asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x00, 0x00, 0x00, 0x00\n"\
                "1:" : : : "rax");
        decrypted[i] = static_cast<char>(crypted[i] ^ ((i % OBF(MOD)) + key));
    }
    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x13, 0x33, 0x37, 0x00\n"\
                "1:" : : : "rax");
    oreturn decrypted;
}

constexpr auto flag = enc_flag(encrypt("YBN24{D3BUGG3R_N3V3R_H34RD_0F_H3R}\n", flag_key), debugger_check);


void setup() {
    setbuf(stdout, nullptr);
    setbuf(stdin, nullptr);
    setbuf(stderr, nullptr);
}

__attribute__((always_inline)) inline void slow_print(const std::string &message, int millis_per_char) {
    ofor (char c : message) {
        std::this_thread::sleep_for(std::chrono::milliseconds(millis_per_char));
        std::cout << c << std::flush;
    }
}

int main() {
    CALL(&setup);

    ptrace(PTRACE_TRACEME, 0, 0, 0);

    asm volatile(\
                "xor %%rax, %%rax\n"\
                "jz 1f\n"\
                ".byte 0x01, 0x02, 0x03, 0x04\n"\
                "1:" : : : "rax");

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(20, 50);

    CALL(&slow_print, OBF("welcome to rev!"), 100);
    std::cout << "\n\n" << std::endl;

    CALL(&slow_print, OBF("please don't debug me >.<"), 50);
    std::cout << "\n" << std::endl;

    CALL(&nothing_sus, sizeof(debugger_check));

    CALL(&slow_print, decrypt(dec_flag(flag, debugger_check), flag_key), 100);
    return 0;
}