#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char c[1001];
    int len = 0,i = 0,sum1 = 0,sum2 = 0;
    while(scanf("%s",c)!=EOF){
        len = strlen(c);
        i=0;
        while(i < len){
            sum1+=(int)(c[i]-'0');
            i+=2;
        }
    //printf("%d\n",sum1);
        i = 1;
        while(i < len){
            sum2+=(int)(c[i]-'0');
            i+=2;
        }
        //prin;tf()
        printf("%d\n",abs(sum1-sum2));
        sum1=0;
        sum2=0;
    }
    return 0;
}
