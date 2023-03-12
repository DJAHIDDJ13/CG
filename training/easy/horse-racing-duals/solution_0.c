#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int N;
    scanf("%d", &N);
    int data[N];
    for (int i = 0; i < N; i++) {
        int Pi;
        scanf("%d", &Pi);
        fprintf(stderr,"%d\n",Pi);
        data[i] = Pi;
    }
    int D = abs(data[0]-data[1]);
    int isOrdered = (data[0] < data[1])? 1: -1;
    for(int i = 0; i < N; i++)
    {
        if(data[i] < data[i+1] && isOrdered == -1)
            isOrdered = 0;
        if(data[i] > data[i+1] && isOrdered == 1)
            isOrdered = 0;
    }
    if(isOrdered == 0)
    {
        for(int i=0;i<N;i++)
        {
            for(int j=i+1;j<N;j++)
            {
                if(abs(data[i]-data[j]) < D)
                    D = abs(data[i]-data[j]);
            }
        }
    }
    else
    {
        for (int i = 1; i < N; i++)
        {
            if(D > abs(data[i-1]-data[i]))
                D = abs(data[i-1] - data[i]);
        }
    }
    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d\n", D);

    return 0;
}
    