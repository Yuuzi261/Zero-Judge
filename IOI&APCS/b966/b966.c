#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

int cmp(const void*, const void*);

int main(void) {
    
    int N, i, start, end;
    int Lines[10000][2];
    ll length;

    while(scanf("%d", &N) != EOF) {

        for(i = 0;i < N;i++)
            scanf("%d %d", &Lines[i][0], &Lines[i][1]);

        qsort(Lines, N, sizeof(int)*2, cmp);

        length = 0;
        start = Lines[0][0], end = Lines[0][1];
        for(i = 1;i < N;i++) {
            if(Lines[i][0] >= end) {
                length += end - start;
                start = Lines[i][0], end = Lines[i][1];
            }
            else if(Lines[i][1] > end)
                end = Lines[i][1];
        }

        length += end - start;
        printf("%d\n", length);

    }

    return 0;

}

int cmp(const void* a, const void* b) {
    return ((int*)a)[0] - ((int*)b)[0];
}
