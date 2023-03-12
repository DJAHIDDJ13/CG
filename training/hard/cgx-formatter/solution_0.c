#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

// read and strip spaces
void read_stripped(char *cgx, int *len)
{
    char c;
    int i = 0;
    while((c = getchar()) != -1) {
        if(isspace(c)) {
            continue;
        }
        switch(c) {
            case '\'':
                cgx[i++] = c;
                while((c = getchar()) != '\'') {
                    cgx[i++] = c;
                }
                cgx[i++] = c;
                break;
            default:
                cgx[i++] = c;
        }
    }
    cgx[i] = '\0';
    *len = i;
}

int main()
{
    int N;
    scanf("%d", &N); fgetc(stdin);
    char cgx[99999];
    int len;
    read_stripped(cgx, &len);
    int tab_level = 0;
    bool print_tabs = false;
    for(int i = 0; i < len; i++) {
        char c = cgx[i];
        switch(c) {
            case '(':
                printf("%c\n", c);
                print_tabs = true;
                tab_level ++;
                break;
            case ')':
                putchar(')');
                tab_level --;
                // lookahead for ;
                if(cgx[i+1] == ';') {
                    puts(";");i++;
                } else {
                    puts("");
                }
                print_tabs = true;
                break;
            case ';':
                puts(";");
                print_tabs = true;
                break;
            case '=':
                putchar('=');
                // lookahead for opening parenthesis
                if(cgx[i+1] == '(') {
                    puts("");
                    print_tabs = true;
                }
                break;
            case '\'':
                // read entire string
                putchar(cgx[i++]); 
                while(cgx[i] != '\'') {
                    putchar(cgx[i++]);
                }
                putchar(cgx[i]);
                // lookahead for closing parenthesis
                if(cgx[i+1] == ')') {
                    puts("");
                    print_tabs = true;
                }
                break;
            case 't':
                printf("%.4s", cgx+i);
                i+=3;
                // lookahead for closing parenthesis
                if(cgx[i+1] == ')') {
                    puts("");
                    print_tabs = true;
                }
                break;
            case 'f':
                printf("%.5s", cgx+i);
                i+=4;
                // lookahead for closing parenthesis
                if(cgx[i+1] == ')') {
                    puts("");
                    print_tabs = true;
                }
                break;
            // default is reserved for digits
            default:
                // read entire integer
                putchar(cgx[i++]);
                while(isdigit(cgx[i])) {
                    putchar(cgx[i++]);
                }
                i--;
                // lookahead for closing parenthesis
                if(cgx[i+1] == ')') {
                    puts("");
                    print_tabs = true;
                }
        }
        if(print_tabs) {
            int num_tabs = tab_level;
            // preemptively remove one tab if the next is closing parenthesis
            // because why the f not
            if(cgx[i+1] == ')')
                num_tabs = num_tabs ? num_tabs-1:0;
            for(int j = 0; j < num_tabs; j++)
                printf("    ");
            print_tabs = false;
        }            
    }
    return 0;
}