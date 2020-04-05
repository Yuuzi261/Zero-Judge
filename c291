#include <stdio.h>
#include <stdlib.h>

int sol(int num,int p[][2]){
    int i = 0,j = 0,t = 0,g = 0;
    int f;
    while(i < num){
        //grouuping
        t = i;
        f=0;
        while( p[t][1]==-1  ){
            f=1;
            p[t][1] = g;
            t = p[t][0];
        }
        if(f == 1)g++;
        ////////////////////////


        i++;
    }
    return g;
}

int main(void){
    int num,i,p = 0;
    int people[50001][2];
    while(scanf("%d",&num)!=EOF){
        i=0;
        while(i < num){
            scanf("%d", &people[i][0]);
            i++;
        }
        i = 0;
        while(i < num){
            people[i][1] = -1;
            i++;
        }
        printf("%d",sol(num,people));
    }
    return 0;
}
