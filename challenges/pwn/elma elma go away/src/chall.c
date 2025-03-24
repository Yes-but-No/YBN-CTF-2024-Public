#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 0x20

char password[8] = "REDACTD\x00";
char* chks[10] = {0};

void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void fun() {
    char doyoupwn[16] = "No I don't";
    int choice;
    printf("Are you sure you pwn?\n\n");
    while (1) {
        if (strcmp(doyoupwn, "Yes I do!") == 0) {
            printf("Hi elma :D\n");
            system("cat flag.txt");
        }

        printf("1. Allocate\n2. Deallocate\n3. Write\n4. Forfeit\n>");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                {
                    int idx;
                    printf("Index (0-9) \n>");
                    scanf("%d", &idx);
                    if (idx < 0 || idx > 9) break;
                    if (chks[idx]) break;

                    chks[idx] = (char *)malloc(BLOCK_SIZE);
                    printf("Chunk %d: %p\n", idx, chks[idx]);
                    break;
                }

            case 2:
                {
                    int idx;
                    printf("Index (0-9) \n>");
                    scanf("%d", &idx);
                    if (idx < 0 || idx > 9) break;
                    if (!chks[idx]) break;

                    free(chks[idx]);
                    break;
                }

            case 3:
                {
                    int idx;
                    printf("Index (0-9) \n>");
                    scanf("%d", &idx);
                    if (idx < 0 || idx > 9) break;
                    if (!chks[idx]) break;

                    printf("Write (Max: 20)\n>");
                    getchar();
                    fgets(chks[idx], 20, stdin);
                    break;
                }
            case 4:
                {
                    printf("Come back when you can pwn.\n");
                    puts(NULL);
                }
            default:
                {
                    printf("DO NOT TEST MY PATIENCE.\n");
                    break;
                }
        }
    }

}

int main() {
    setup();
    FILE *file = tmpfile();
    char buf[8];

    printf("Do as you wish to the tmpfile :) \n>");
    scanf("%128s", (char*)file);

    fread(buf, 1, 8, file);
    printf("Here's an excerpt of what's in the tmpfile: %s\n", buf);

    printf("Do you pwn?\n>");
    scanf("%7s", buf);
    buf[7] = 0x00;
    if (strcmp(password, buf) != 0) {
        printf("You clearly do not pwn.\n");
        return -1;
    }

    fun();
    return 0;
}