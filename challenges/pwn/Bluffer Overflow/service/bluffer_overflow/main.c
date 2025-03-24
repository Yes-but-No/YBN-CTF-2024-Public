#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

void ignore_me_init_buffering(){
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int main(){
	ignore_me_init_buffering();
	char duckSpeak[] = "honk";
	puts("One of us is lying, One of us is telling the truth, One of us is actually a duck");
	puts("1. Person number 2 is a the liar, he doesnt have the flag. I am telling the truth!");
	puts("2. Quack.");
	puts("3. Person number 1 does not have the flag");
	puts("Who has the flag?");
	char input[16];
	gets(input);
	if (strcmp(input, "3") == 0){
		puts("blep");
		if (strcmp(duckSpeak, "quack") == 0){
			execve("/bin/sh", NULL, NULL);
		}
	} else {
		puts("bleh");
	}

	return 0;
}
