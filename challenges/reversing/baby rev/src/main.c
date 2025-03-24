#include <stdio.h>
#include <string.h>

char password[] = "YBN24{s3per_s3cur3_p4ssw0rd_but_h0w_d0_1_st0r3_it?}";

int main() {
    printf("Whats the password?\n>> ");
    char input[100];
    scanf("%99s", input);
    if(!strcmp(password, input)) {
        printf("Correct!\n");
    } else {
        printf("Wrong!");
    }
    return 0;
}
