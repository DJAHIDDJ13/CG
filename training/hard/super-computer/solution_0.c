#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    int* x = (int*)a;
    int* y = (int*)b;
    return x[1] - y[1];
}

int main() {
    int n, i, end = 0, count = 0;
    scanf("%d", &n);
    int activities[n][2];
    for (i = 0; i < n; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        activities[i][0] = a;
        activities[i][1] = a + b;
    }
    qsort(activities, n, sizeof(activities[0]), cmp);
    for (i = 0; i < n; i++) {
        if (activities[i][0] >= end) {
            end = activities[i][1];
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}