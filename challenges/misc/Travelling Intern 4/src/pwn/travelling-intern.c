#include <stdio.h>
#include <unistd.h>

void win() {
    char *args[] = {"/bin/cat", "flag.txt", NULL};
    execve(args[0], args, NULL);
}

void get_feedback() {
    char feedback[64];
    fgets(feedback, 0x64, stdin);
    return;
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    puts("On a scale of 1 - 10, how hard was this OSINT challenge?");
    printf("> ");
    fflush(stdout);

    get_feedback();

    puts("Here's the flag: ...");
    puts("Or not :3");
    fflush(stdout);

    return 0;
}
