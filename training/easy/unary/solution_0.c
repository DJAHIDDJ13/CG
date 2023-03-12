#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    char MESSAGE[101];
    fgets(MESSAGE, 101, stdin);
    char message[101*7] = {0};
    for(int i=0;i<strlen(MESSAGE)*7;i++)
        message[i] = '0';
    for(int i=0;i<strlen(MESSAGE)-1;i++)
    {
        int n = MESSAGE[i];
        int remain;
        int j = 6;
        while(n!=0)
        {
            remain = n % 2;
            n /= 2;
            
            if(remain == 0)
                message[i*7+j] = '0';
            else if(remain == 1)
                message[i*7+j] = '1';
            j--;
            }
    }
   // fprintf(stderr, "strlen(MESSAGE) = %d\n", n);
    message[7*strlen(MESSAGE)-7] = 0;
    int l = strlen(message);
    for(int i=0;i<l;i++){
        if(message[i-1] != message[i] || i == 0)
        {
            if(i != 0){
                if(message[i] == '0')
                    printf(" 00 0");
                else
                    printf(" 0 0");}
            else{
                if(message[i] == '0')
                    printf("00 0");
                else
                    printf("0 0");}
        }
        else{
            printf("0");
        }
    }
    fprintf(stderr, "\n%s\n",message);

    return 0;
}
