#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Don't let the machines win. You are humanity's last hope...
 **/
void getNeighbours(int iy,int jx,int height,int width, char ** matrix)
{
    int x0 = jx;
    int y0 = iy;
    int x1 = -1;
    int y1 = -1;
    int x2 = -1;
    int y2 = -1;
    
    // right neighbour
    for(int j = jx+1; j < width; j++) {
        if(matrix[iy][j] == '0') {
            x1 = j;
            y1 = iy;
            break;
        }
    }
    // down
    for(int i = iy+1; i < height; i++) {
        if(matrix[i][jx] == '0') {
            x2 = jx;
            y2 = i;
            break;
        }
    }
    
    printf("%d %d %d %d %d %d\n", x0, y0, x1, y1, x2, y2);
}
int main()
{
    int width; // the number of cells on the X axis
    scanf("%d", &width);
    int height; // the number of cells on the Y axis
    scanf("%d", &height); fgetc(stdin);
    char ** matrix;
    matrix = malloc(sizeof(char*) * height);
    for (int i = 0; i < height; i++) {
        char line[32]; // width characters, each either 0 or .
        fgets(line, 32, stdin); // width characters, each either 0 or .
        matrix[i] = malloc(sizeof(char)*width);
        for(int j = 0; j < width; j++) {
            matrix[i][j] = line[j];
        }
    }

    
    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    for(int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
            if(matrix[i][j] == '.') {
                continue;
            }
            getNeighbours(i,j, height, width, matrix);
        }
    }

return 0;
}
