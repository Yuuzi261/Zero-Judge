#include <stdio.h>
#include <stdlib.h>

int arr[100000],len = 100000,front = 0,back = 0,empty = 1;

struct Node{
	int* nb;
	int nbLen;
	int color;
	int from;
	int d;
};

struct Node N[100000];

int enqueue(int n);
int dequeue();
int isFull();
int isEmpty();
void printQueue();
void Traverse();

int main(void){
	int i = 0,k = 0,x,y;
	int n,e,j,max,maxind;
	while(scanf("%d",&n) != EOF){
		for(i = 0;i < n+1;i++)N[i].nbLen = 0;
		e = n - 1;
		for(i = 0;i < e;i++){
			scanf("%d %d",&x,&y);
			N[x].nbLen++;
  			N[x].nb = realloc( N[x].nb, N[x].nbLen * sizeof(int) );
			N[x].nb[N[x].nbLen-1] = y;
			N[y].nbLen++;
			N[y].nb = realloc( N[y].nb, N[y].nbLen * sizeof(int) );
			N[y].nb[N[y].nbLen-1] = x;
		}
		for(i = 0;i < n;i++){
			N[i].color = 0;
			N[i].from = -1;
			N[i].d = n+1;
		}
		N[0].color = 1;
		enqueue(0);
		N[0].d = 0;
		while(empty != 1)Traverse();
		max = -1;
		maxind = -1;
		for(i = 0;i < n;i++){
			if(N[i].d > max){
				max = N[i].d;
				maxind = i;
			}
		}
		for(i = 0;i < n+1;i++){
			N[i].color = 0;
			N[i].from = -1;
			N[i].d = n+1;
		}
		N[maxind].color = 1;
		enqueue(maxind);
		N[maxind].d = 0;
		while(empty != 1)Traverse();
		max = -1;
		maxind = -1;
		for(i = 0;i < n;i++){
			if(N[i].d > max){
				max = N[i].d;
				maxind = i;
			}
		}
		printf("%d\n",max);
	}
	return 0;
}

void Traverse(){
	int p,i,t;
	p = dequeue();
	for(i = 0;i < N[p].nbLen;i++){
		t = N[p].nb[i];
		if(N[t].color == 0){
			N[t].color = 1;
			
			enqueue(t);
			N[t].from = p;
			N[t].d = N[p].d+1;
		}
		N[p].color = 2;
	}
}

int isFull(){
	if(front == back && empty != 1)return 1;
	else return 0;
}

int isEmpty(){
	if(front == back && empty == 1)return 1;
	else return 0; 
}

int dequeue(){
	int ans;
	if(empty == 1){
		printf("empty!!\n");
		return 0;
	}
	else{
		ans = front;
		front++;
		if(front == len)front%=len;
		if(front == back)empty = 1;
	}
	return arr[ans];
}

int enqueue(int n){
	if(front != back || empty == 1){
		arr[back] = n;
		back++;
		if(back == len)back%=len;
	}
	else{
		printf("The Queue is full!!\n");
	}
	empty = 0;
}

void printQueue(){
	int i;
	if(front < back){
		for(i = front;i < back;i++)printf("%d ",arr[i]);
	}
	else if(front > back){
		for(i = front;i < len;i++)printf("%d ",arr[i]);
		for(i = 0;i < back;i++)printf("%d ",arr[i]);
	}
	else{
		if(empty != 1){
			for(i = front;i < len;i++)printf("%d ",arr[i]);
			for(i = 0;i < back;i++)printf("%d ",arr[i]);
		}
		else{
			printf("The Queue is empty!!");
		}
	}
	printf("\n");
}
