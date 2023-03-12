#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position

    scanf("%d%d%d%d", &lightX, &lightY, &initialTX, &initialTY);
    int currentX = initialTX;
    int currentY = initialTY;
    // game loop
    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        scanf("%d", &remainingTurns);
        int moveX = currentX - lightX;
        int moveY = currentY - lightY;
        // Write an action using printf(). DON'T FORGET THE TRAILING \n
        // To debug: 
        if(moveX!=0 && moveY!=0)
        {
            if(moveX > 0 && moveY >0){
                printf("NW\n");
                currentX --;
                currentY --;
            }
            if(moveX < 0 && moveY >0){
                printf("NE\n");
                currentX ++;
                currentY --;
            }
            if(moveX < 0 && moveY <0){
                printf("SE\n");
                currentX ++;
                currentY ++;
            }
            if(moveX > 0 && moveY <0){
                printf("SW\n");
                currentX --;
                currentY ++;
            }
        }
        else{
            if(moveX == 0)
            {
                if(moveY < 0){
                    printf("S\n");
                    currentY ++;
                }
                if(moveY > 0){
                    printf("N\n");
                    currentY --;
                }
            }
            if(moveY == 0)
            {
                if(moveX > 0){
                    printf("W\n");
                    currentX --;
                }
                if(moveX < 0){
                    printf("E\n");
                    currentX ++;
                }
            }
        }
        // A single line providing the move to be made: N NE E SE S SW W or NW
    }

    return 0;
}