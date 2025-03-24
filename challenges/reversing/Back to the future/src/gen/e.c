#include <stdio.h>
#include <stdint.h>

uint32_t xorshift32(uint32_t x) {
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

int main() {
    char str[] = "Now for a really bad animation of a clock!\n";
    for(int i = 0; i < sizeof(str); i++) {
        printf("\\x%02x", str[i]^0x32);
    }
    puts("");
    FILE *fp = fopen("re_written.txt", "r");
    if(fp == NULL) {
        perror("fopen");
        return 1;
    }

    char ch;
    uint32_t count = 0;
    uint32_t seed, tmp;
    seed = tmp = 0xab3d2f3;
    printf("char duck_roll[] = {");
    while((ch = fgetc(fp)) != EOF) {
        tmp = xorshift32(tmp);
        printf("0x%02x, ", (ch ^ tmp) & 0xff);
        count++;
    }
    puts("};");

    printf("unsigned char duck_roll_enc[] = {");
    for(int i = 0; i < count; i++) {
        seed = xorshift32(seed);
        printf("0x%02x, ", (seed) & 0xff);
    }
    puts("};");

    char got_tricked[] = "Ha! Just kidding! You got DUCK-ROLLED!\n[Warning] The lyrics of Rick'rolln has been modified!\n";
    for(int i = 0; i < sizeof(got_tricked); i++) {
        printf("\\x%02x", got_tricked[i]^0xa5);
    }
    puts("");

    return 0;
}
