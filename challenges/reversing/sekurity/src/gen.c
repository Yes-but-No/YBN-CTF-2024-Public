#include <stdio.h>
#include <string.h>

void swap(char *buf, long x, long y) {
    char tmp = buf[x];
    buf[x] = buf[y];
    buf[y] = tmp;
    return;
}

int main() {
    char flag[] = "YBN24{s3kur1ty_thr0u4h_m1x1ng_1n_a_c4udr0n}";
    char key[] = "}nb!{y?";
    for(int i = 0; i < strlen(flag); i++) {
        char index = key[i % strlen(key)];
        if((i & 3) != 0) {
            unsigned int tmp = index % strlen(flag);
            swap(flag, i, tmp);
            printf("%d, ", tmp);
        }
    }
    printf("\n%s\n", flag);
    return 0;
}
