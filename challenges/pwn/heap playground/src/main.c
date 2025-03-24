#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ignore_me_innit_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

char *flag_ptr = 0;

void read_flag() {
    FILE *fp = fopen("flag.txt", "r");
    // eh, I know the flag
    long len = 47;
    if(fp == NULL) {
        fprintf(stderr, "Error! `flag.txt` not found! If this is the challenge instance, please open a ticket!\n");
        exit(-1);
    } else {
        flag_ptr = calloc(1, len);
        fread(flag_ptr, 1, len-1, fp);
    }
    flag_ptr[len-1] = '\x00';
    fclose(fp);
    return;
}

char *string_ptrs[16] = {};

void allocate_str() {
    int len = 0;
    printf("Input string length (including null terminator): ");
    scanf("%d", &len);
    getchar(); // gets newline
    if(len <= 1) { // Thats a weird sized string...
        puts("Invalid string size!");
        return;
    }
    char *tmp = calloc(1, len);
    if(tmp == NULL) {
        exit(-1);
        return;
    }
    char check = 0;
    for(int i = 0; i < len-1; i++) {
        if((check = fgetc(stdin)) == '\n') {
            break;
        }
        tmp[i] = fgetc(stdin);
    }
    tmp[len-1] = 0;
    printf("Which string number do you want to store it in?\n"
            "[0-15]>> ");
    scanf("%d", &len);
    if(len >= 0 && len < 16) {
        string_ptrs[len] = tmp;
        printf("string %d: '%s' saved!\n", len, string_ptrs[len]);
    }
}

void read_str() {
    int index = 0;
    printf("What string do you want to read?\n"
            "[0-15]>> ");
    scanf("%d", &index);
    if(index >= 0 && index < 16) {
        if(string_ptrs[index] != NULL) {
            printf("string %d: %s\n", index, string_ptrs[index]);
        } else {
            puts("NULL string detected!");
        }
    }
}

void free_str() {
    int index = 0;
    printf("What string do you want to free?\n"
            "[0-15] >> ");
    scanf("%d", &index);
    if(index >= 0 && index < 16) {
        if(string_ptrs[index] != NULL) {
            free(string_ptrs[index]);
            printf("string %d has been freed!\n", index);
        }
    }
}

int main() {
    ignore_me_innit_buffering();
    int choice = 0;
    puts("Welcome to my heap playground!");
    while(1) {
        // main execution!
        puts("What would you like to do?");
        puts("-------------------------------");
        puts("[0]\tAllocate string");
        puts("[1]\tRead string");
        puts("[2]\tFree string");
        puts("[3]\tGet flag # hey, just because I fetch it doesn't mean you'll be able to read it! MUAHAHA!");
        puts("[4]\texit!");
        printf(">> ");
        scanf("%d", &choice);
        if(choice == 0) {
            allocate_str();
        } else if(choice == 1) {
            read_str();
        } else if(choice == 2) {
            free_str();
        } else if(choice == 3) {
            read_flag();
        } else if(choice == 4) {
            return 0;
        }
    }
    return 0;
}
