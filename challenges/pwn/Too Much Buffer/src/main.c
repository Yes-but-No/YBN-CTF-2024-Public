#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
    system("cat flag.txt");
    return;
}

void ignore_me_innit_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int valid_characters(char str) {
    char ch = str;
    int rval = -1;
    char *what = "yesbutnoYESBUTNO";
    for(size_t i = 0; i < strlen(what); i++) {
        if(what[i] == ch) {
            rval = i;
            break;
        }
    }
    return rval;
}

#define BUF_SIZE 100

char err[] = " ____        _         __  __                 _\n| __ ) _   _| |_ ___  |  \\/  | ___  _ __  ___| |_ ___ _ __\n|  _ \\| | | | __/ _ \\ | |\\/| |/ _ \\| '_ \\/ __| __/ _ \\ '__|\n| |_) | |_| | ||  __/ | |  | | (_) | | | \\__ \\ ||  __/ |\n|____/ \\__, |\\__\\___| |_|  |_|\\___/|_| |_|___/\\__\\___|_|\n       |___/";

int main() {
    ignore_me_innit_buffering();
    puts(err);
    puts("I eat bits with mushrooms, bits with muffins, and even bits with bits!");
    char buf[BUF_SIZE];
    scanf("%s", buf);
    size_t len = strlen(buf);
    for(unsigned long int i = 0; i < len; i++) {
        if(-1 == valid_characters(buf[i])) {
            goto ew;
        }
    }
    if(len < BUF_SIZE) {
        char *ptr = buf;
        if(len > 4) {
            ptr = buf + len - 4;
        }
        printf("Most yummy part(also the last part): %s\n", ptr);
    } else {
ew:
        puts("ewwwwwwwwwwwwwwwwwww what'd you put in that????");
        exit(0);
    }
    return 0;
}
