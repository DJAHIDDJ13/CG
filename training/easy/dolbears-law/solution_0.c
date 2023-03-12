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
    int M;
    scanf("%d", &M); fgetc(stdin);
    float N60 = 0.0, N8 = 0.0;
    int total_sum;
    int last_elem = 0;
    for (int i = 0; i < M; i++) {
        int arr[15];
        int j = 0;
        while (j < 15 && scanf("%d", &arr[j++]) == 1)
            ;
        float sum = 0.0;
        for(j = 0; j < 15; j++) {
            sum += arr[j];
            total_sum += arr[j];
            last_elem = arr[j];
        }
        N60 += 10.0 + (sum - 40.0) / 7.0;
    }
    if(M % 2==1) total_sum -= last_elem;

    N60 = N60 / M;
    int num_pairs = M*15/2;
    N8 = (total_sum + 5.0 * num_pairs) / num_pairs;

    printf("%.1f\n", N60);
    if(5<=N60 && N60<=30)
        printf("%.1f\n", N8);

    return 0;
}