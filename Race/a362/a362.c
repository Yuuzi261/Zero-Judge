#include <stdio.h>
#include <stdlib.h>

struct STATUE{
    int height;
    int weight;
    int index;
};

typedef struct STATUE statue;
statue L[10001];

void swap(int j){
    int temp;
    temp = L[j].height;
    L[j].height = L[j+1].height;
    L[j+1].height = temp;

    temp = L[j].weight;
    L[j].weight = L[j+1].weight;
    L[j+1].weight = temp;

    temp = L[j].index;
    L[j].index = L[j+1].index;
    L[j+1].index = temp;
}

int main(){
    int n, i, j, ans;
    while(scanf("%d", &n) != EOF){

        for(i = 0;i < n;i++){
            scanf("%d %d", &L[i].height, &L[i].weight);
            L[i].index = i;
        }

        for(i = 0;i < n - 1;i++)
            for(j = 0;j < n - i - 1;j++){
                if((L[j].height > L[j+1].height) || ((L[j].height == L[j+1].height) && (L[j].weight > L[j+1].weight))){
                    swap(j);
                }
            }

        ans = 0;
        for(i = 0;i < n;i++)
            for(j = 0;j < n;j++){
                if(L[j].index == i)
                    ans += abs(j - i);
            }

        printf("%d\n", ans);
    }
    return 0;
}
