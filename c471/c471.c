#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

int cmp(const void*, const void*);
ll printEnergy(int items[100000][2], int);

int main(void) {

    int N, i;
    int items[100000][2];
    
    while(scanf("%d", &N) != EOF) {
        for(i = 0;i < N;i++) scanf("%d", &items[i][0]);
        for(i = 0;i < N;i++) scanf("%d", &items[i][1]);
        qsort(items, N, sizeof(int)*2, cmp);
        printf("%lld\n", printEnergy(items, N));
    }

    return 0;

}

int cmp(const void* a, const void* b) {
    return ((int*)a)[0] * ((int*)b)[1] - ((int*)b)[0] * ((int*)a)[1];
}

ll printEnergy(int items[100000][2], int N) {

    ll energy = 0, weight = 0;

    for(int i = 1;i < N;i++) {

        weight += items[i - 1][0];
        energy += weight * items[i][1];

    }

    return energy;

}
