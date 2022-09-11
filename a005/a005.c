#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c,d,e,f;
    while(scanf("%d",&a)!=EOF)
    {
        for(int i=0;i<a;i++){
            scanf("%d %d %d %d",&b,&c,&d,&e);
            if(c-d==d-c || e-d==d-c){
                f=e+(d-c);
                printf("%d %d %d %d %d\n",b,c,d,e,f);
            }
            else{
                f=e*(d/c);
                printf("%d %d %d %d %d\n",b,c,d,e,f);
            }
        }
    }
}
