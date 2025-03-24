#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int check = 42;
int main() { 
    ignore_me_init_buffering();
    printf("Welcome to our amazing instant recall system! Our memory is so good we can instantly recall what you wrote!");
    while (1) {
        char buf[32];
        printf("\nInput: ");
        fgets(buf, 31, stdin);
        printf(buf);
        if (check == 69){
            system("cat flag.txt");
            break;
        }
    }

    return 0;
}
