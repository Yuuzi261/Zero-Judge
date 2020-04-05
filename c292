#include <stdio.h>
#include <stdlib.h>
struct cordin{
	int x;
	int y;
};

int dec,cnt = 0,n = 0;
int larr[50000];
struct cordin c;

void move(int narr[][50]){
	if(dec==0)c.x-=1;
	else if(dec==1)c.y-=1;
	else if(dec==2)c.x+=1;
	else c.y+=1;
	larr[n] = narr[c.y][c.x];
	n++;
	cnt++;
}

void dechange(){
	if(dec==0)dec = 1;
	else if(dec==1)dec = 2;
	else if(dec==2)dec = 3;
	else dec = 0;
}

void printnl(int num){
	int i = 0;
	for(i = 0;i < num*num-1;i++)printf("%d",larr[i]);
}

int main(int argc, char *argv[]) {
	int num,i = 0,j = 0,k = 0;
	int narr[50][50];
	while(scanf("%d",&num)!=EOF){
		scanf("%d",&dec);
		for(i = 0;i < num;i++)
			for(j = 0;j < num;j++)scanf("%d",&narr[i][j]);
		c.x = ((num + 1)/2)-1;
		c.y = ((num + 1)/2)-1;
		printf("%d",narr[c.y][c.x]);
		cnt = 0;
		i = 1;
		while(cnt < num*num){
			for(k = 0;k < i;k++)move(narr);
			dechange();
			for(k = 0;k < i;k++)move(narr);
			dechange();
			i++;
		}
		printnl(num);
		cnt = 0;
	}
	return 0;
}
