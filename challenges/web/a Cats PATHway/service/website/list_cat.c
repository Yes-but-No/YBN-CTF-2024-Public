#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    // C in website???? no wayyyy
    if (setuid(0) == -1) {
        perror("setuid failed");
        return 1;
    }

    int ret_code = system("ls ./backend");

    if (ret_code == -1) {
        perror("system failed");
        return 1;
    }

    return 0;
}
