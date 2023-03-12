#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int N;
    scanf("%d", &N); fgetc(stdin);
    int log[10] = {0};
    for (int i = 0; i < N; i++) {
        char transaction[33];
        scanf("%[^\n]", transaction); fgetc(stdin);

        for(int j = 0; j < strlen(transaction); j++) {
            if(transaction[j] >= '1' && transaction[j] <= '9') {
                log[transaction[j]-'1'] ++;
                break;
            }
        }
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    double ben[] = {30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6};
    for(int i = 0; i < 9; i++) {
        if(abs(log[i] * 100.0 / N - ben[i]) > 10) {
            printf("true\n");
            exit(0);
        }
    }
    printf("false\n");

    return 0;
}