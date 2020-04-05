#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void sol(int a,int b,int c);

int main(void){
	int a,b,c;
	while(scanf("%d",&a) != EOF){
		scanf("%d %d",&b,&c);
		if(b*b - 4*a*c < 0)printf("No real root");
		else sol(a,b,c);
	}
	return 0;
}

void sol(int a,int b,int c){
	int a1,a2;
	a1 = (sqrt(b*b - 4*a*c) - b)/(a*2);
	a2 = (b*(-1) - sqrt(b*b - 4*a*c))/(a*2);
	if(a1 == a2)printf("Two same roots x=%d",a1);
	else printf("Two different roots x1=%d , x2=%d",a1,a2);
}
