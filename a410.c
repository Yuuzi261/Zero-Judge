#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a,b,c,d,e,f;
	float dx,dy,del;
	while(scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f) != EOF){
		dx = (c*e-b*f);
		dy = (a*f-c*d);
		del = (a*e-b*d);
		if(dx == 0 && dy ==0 && del ==0)printf("Too many\n");
		else if(del == 0 && (dx != 0 || dy != 0))printf("No answer\n");
		else{
			printf("x=%.2f\n",dx/del);
			printf("y=%.2f\n",dy/del);
		} 
	}
	return 0;
}
