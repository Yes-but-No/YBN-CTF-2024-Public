#include <stdio.h>
#include <stdint.h>
#include <sys/syscall.h>
#include <unistd.h>

void ignore_me_innit_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

long number = 0x13e; // WHY IS THERE LIKE 3 DIFF SYSCALL NUMBERS GRR
                     // Oh it was because of different architectures lol

char arg0[100];
unsigned int arg1 = 10;
unsigned int arg2 = 0;

void station_0() {
    puts("Checking station!");
    printf("train number:  0x%02lx\n", number);
    printf("hmm?: %s\n", arg0);
    printf("carriage: %d\n", arg1);
    printf("station number: %d\n", arg2);
    printf("\n");
}

void station_1() {
    puts("Alright! Lets get moooving!");
}

unsigned char enable_me = 0;

void station_2() {
    enable_me = 1;
}

void station_3() {
    printf("Enter train number: ");
    scanf("%lu", &number);
}

void station_4() {
    printf("Enter carriage: ");
    scanf("%u", &arg1);
}

void station_5() {
    printf("Enter station number: ");
    scanf("%u", &arg2);
}

void final_station() {
    if(enable_me == 1) {
        syscall(number, arg0, arg1, arg2);
    }
}


void unimportant_station() {
    static volatile char bin_bash[] = "/bin/bash";
    for(int i = 0; i < sizeof(bin_bash); i++) {
        arg0[i] = bin_bash[i];
    }
}


int main() {
    ignore_me_innit_buffering();
    puts("Hello there, instructor!");
    puts("Your mission is to travel to every station! In each station, you can configure different parameters. \n"
         "Give it a shot!");
    printf("Heres the address to your first station: %p\n", station_0);

    void *ptr;
    //void (*f_ptr)();
    while(1) {
        printf("Where'd you wanna go?\n>> ");
        scanf("%p\n", &ptr); // get newline yahoo!
        ((void (*)())ptr)(); // It'll work out, trust.
    }

    return 0;
}
