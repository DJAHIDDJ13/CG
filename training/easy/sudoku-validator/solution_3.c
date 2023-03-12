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
    int sums[3][3][9] = {0};
    int v_sums[9][9] = {0};
    int h_sums[9][9] = {0};
    for (int i = 0; i < 9; i++) {

        for (int j = 0; j < 9; j++) {
            int n;
            scanf("%d", &n);
            sums[(int)(i/3)][(int)(j/3)][n-1] = 1;
            h_sums[j][n-1] = 1;
            v_sums[i][n-1] = 1;
        }
    }
    bool res = true;
    for(int i = 0; i < 9; i++) {
        int a = i/3;
        int b = i%3;
        int sum1 = 0, sum2 = 0, sum3 = 0;
        for(int j = 0; j < 9; j++) {
            sum1 += sums[a][b][j];
            sum2 += v_sums[i][j];
            sum3 += h_sums[i][j];
        }
        if(sum1 != 9 || sum2 != 9 || sum3 != 9) {
            res = false;
            break;
        }
    }

    if(res) {
        printf("true\n");
    } else {
        printf("false\n");
    }
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");


    return 0;
}