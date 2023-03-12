#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
void split(char ch[], char spl[100][10])
{
    int count = 0;
    int j = 0;
    for(int i=0;i<strlen(ch);i++)
    {
        if(ch[i] != ' ')
        {
            spl[count][j] = ch[i];
            j++;
        }
        else
        {
            spl[count][j] = 0;
            count ++;
            j = 0;
        }

    }
}
int main()
{
    int n; // the number of temperatures to analyse
    scanf("%d", &n); fgetc(stdin);
    char temps[257]; // the n temperatures expressed as integers ranging from -273 to 5526
    fgets(temps, 257, stdin); // the n temperatures expressed as integers ranging from -273 to 5526
    char splitted[n][10];
    split(temps, splitted);
    int realTemps[n];
    for(int i=0;i<n;i++)
    {
        realTemps[i] = atoi(splitted[i]);
    }
    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: 
    int closest = (n == 0)? 0 : realTemps[0];
    for(int i=0;i<n;i++)
    {
        if(abs(realTemps[i]) < abs(closest))
            closest = realTemps[i];
        else if (abs(realTemps[i]) == abs(closest))
          closest = (realTemps[i] < closest)? closest: realTemps[i];
    }
    printf("%d\n", closest);

    return 0;
}