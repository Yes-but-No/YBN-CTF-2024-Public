#include <stdio.h>
#include <string.h>

int main() {
    puts("Home-made password checker 999999 (biger numbers are cool!)");
    printf("What is the password? \n>> ");
    fflush(stdout);
    char input[101];
    scanf("%100s", input);
    size_t in_len = strlen(input);
    char flag[] = "}yAd_y4ev3_y4D_lLA_sGniRts_kc47s_gnIpp1LF{42NBY";
    if(in_len != strlen(flag)) {
        goto wrong_flag;
    }
    size_t j = 0;
    for(size_t i = in_len-1; i > 0; i--) {
        if(flag[j] != input[i]) {
            goto wrong_flag;
        }
        j++;
    }
    puts("Correct password!");
    return 0;
wrong_flag:
    puts("Wrong password!");
    return 1;
}
