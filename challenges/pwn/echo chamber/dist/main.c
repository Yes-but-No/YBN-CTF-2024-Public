#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ignore_me_innit_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void win() {
    system("/bin/sh");
    exit(1);
}


int main() {
    ignore_me_innit_buffering();
    char check[] = "stack check check stack";
    char input[50];
    while(1) {
        printf("+--- Echo chamber! ---+\n>> ");
        gets(input);
        printf("You said: ");
        puts(input);

        if(strcmp(check, "stack check check stack")) {
            // it should never go here!
            puts("huh..? What happened? Shell for debug!");
            win();
        }
    }
    return 0;
}
