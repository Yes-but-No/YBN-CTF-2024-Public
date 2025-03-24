#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

void ignore_me_init_buffering(){
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int win(){
  execve("/bin/sh", NULL, NULL);
	return 0;
}

int main(){
	ignore_me_init_buffering();
	printf("what does the yellow bird say?\n");
	char input[16];
	gets(input);
	if (strcmp(input, "chirp") == 0){
		printf("The yellow bird chirps!");
		exit(1);
	} else {
		printf("The yellow bird does NOT say: ");
		printf(input);
		printf("\nLets try that again\n");
		printf("what does the yellow bird say?\n");
		gets(input);
		if (strcmp(input, "chirp") == 0){
			printf("The yellow bird chirps!");
			exit(1);
		} else {
			printf("nevermind.");
		}
	}

	return 0;
}
