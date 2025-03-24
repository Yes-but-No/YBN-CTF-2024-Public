#include <stdio.h>
#include <string.h>

int main() {
    char flag[] = "YBN24{FL1ppIng_s74ck_stRinGs_ALl_D4y_3ve4y_dAy}";
    size_t len = strlen(flag);
    printf("size_t len = %lu;\n", len);
    printf("char flag[] = \"");
    for(int i = len; i >= 0; i--) {
        printf("%c", flag[i]);
    }
    printf("\";\n");
    return 0;
}
