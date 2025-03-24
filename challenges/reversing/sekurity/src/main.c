#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
24, 12, 33, 35, 20, 39, 12, 33, 37, 20, 39, 24, 33, 37, 35, 39, 24, 12, 37, 35, 20, 24, 12, 33, 35, 20, 39, 12, 33, 37, 20, 39,
"Y1ta4c4rkN2uxs3Bhr1{n_tu_0uyg_mr_dnh4n1}0_1"
 */

void swap(char *buf, long x, long y) {
    char tmp = buf[x];
    buf[x] = buf[y];
    buf[y] = tmp;
    return;
}

int main() {
    char flag[] = "Y1ta4c4rkN2uxs3Bhr1{n_tu_0uyg_mr_dnh4n1}0_1";
    char key[] = "}nb!{y?";

    char buf[100];
    puts("Really High Security Vault 100,000.");
    printf("Please enter the passcode: ");
    scanf("%99s", buf);
    size_t len = strlen(buf);
    size_t f_len = strlen(flag);
    if(len == f_len) {
        for(size_t i = 0; i < f_len; i++) {
            char index = key[i % strlen(key)];
            unsigned char tmp = index % strlen(flag);
            if((i & 3) != 0) {
                swap(buf, i, tmp);
            }
        }
        if(strcmp(flag, buf) == 0) {
            puts("Correct passcode! Welcome!");
            exit(0);
        }
    }
    puts("Wrong passcode! Exiting!");
    return 0;
}
