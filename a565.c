#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char S[10000000];

int main(){
    int n, i, j, count, Slen, pcount, ans;
    while(scanf("%d", &n) != EOF){
        count = 0;
        for(i = 0;i < n;i++){
            scanf("%s", &S);
            Slen = strlen(S);
            pcount = 0, ans = 0;
            for(j = 0;j < Slen;j++){
                if(S[j] == 'p')
                    pcount++;
                else if(S[j] == 'q'){
                    if(pcount > 0){
                        ans++;
                        pcount--;
                    }
                }
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}
