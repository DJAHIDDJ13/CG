#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
struct decode_tree {
    int ascii;
    struct decode_tree *z_child;
    struct decode_tree *o_child;
};

int main()
{
    struct decode_tree *head = calloc(1, sizeof(struct decode_tree));
    struct decode_tree *p = head;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        char b[5001] = {0};
        int c;
        scanf("%s%d", b, &c);
        // build the tree
        for(int j = 0; j < strlen(b); j++) {
            int ch = b[j];
            if(ch == '1') {
                if(p->o_child == NULL) {
                    p->o_child = calloc(1, sizeof(struct decode_tree));
                }
                p = p->o_child;
            } else if(ch == '0') {
                if(p->z_child == NULL) {
                    p->z_child = calloc(1, sizeof(struct decode_tree));
                }
                p = p->z_child;                
            }
        }
        p->ascii = c;
        p = head;
    }
    
    char s[5001];
    scanf("%s", s);
    char res[5001] = {0};
    int idx = 0;
    int i = 0;
    int err_idx = 0;
    // parse using the tree
    for(i = 0; i < strlen(s); i++) {
        char c = s[i];
        if(c == '1') {
            if(p->o_child == NULL) {
                printf("DECODE FAIL AT INDEX %d\n", err_idx);
                exit(0);
            }
            if(p->o_child != NULL) 
                p = p->o_child;
        } else if (c == '0') {
            if(p->z_child == NULL) {
                printf("DECODE FAIL AT INDEX %d\n", err_idx);
                exit(0);
            }
            if(p->z_child != NULL)
                p = p->z_child;
        }
        if (p->o_child == NULL && p->z_child == NULL){
            res[idx++] = p->ascii;
            err_idx = i;
            p = head;
        }
    }
    if(p != head) {
        printf("DECODE FAIL AT INDEX %d\n", i-1);
        exit(0);
    }
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%s\n",res);

    return 0;
}