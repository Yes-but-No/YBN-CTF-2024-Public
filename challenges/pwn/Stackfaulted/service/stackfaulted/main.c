#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
    ignore_me_init_buffering();
    char loadingFunction[64] = {0}; 
    char privilege[8] = "USER"; 
    char input[32];
    puts("Enter password: ");
    gets(input);
    if (strcmp(input, "verySecurePassword123") != 0){
        exit(1);
    }
    if (strcmp(privilege, "ADMIN") ==0){
        puts("The admin console is still under construction, come back later");
        void (*loadingFunc)() = (void (*)())loadingFunction;
        loadingFunc();
    }else{
        puts("Program exited successfully");
        exit(0);
    }
    return 0;
}

