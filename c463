#include <stdio.h>
#include <stdlib.h>

int arr[100001],len = 100001,front = 0,back = 0,empty = 1;

struct Node{
	int parent;
	int* child;
	int chdLen;
	int color;
	int from;
	int d;
	int T;
};

struct iNd{
	int ind;
	int d;
};

struct iNd *leaf;
struct Node N[100001];

int enqueue(int n);
int dequeue();
int isFull();
int isEmpty();
void printQueue();
void printParent(int n);
void printChild(int n);
void BFS(int n);
void Height(int a,int n);
int CMP(const void* a,const void* b);

int main(void){
	int i,t,r,l,a,ad,f,c;
	int n,e,j;//,ans = 0;
	long long ans = 0;
	while(scanf("%d",&n) != EOF){
		front = 0;
		back = 0;
		empty = 1;
		for(i = 1;i <= n;i++){
			N[i].chdLen = 0;
			N[i].parent = -2;
		}
		for(i = 1;i <= n;i++){
			scanf("%d",&e);
			for(j = 0;j < e;j++){
				scanf("%d",&t);
				N[i].chdLen++;
				N[i].child = realloc( N[i].child, N[i].chdLen * sizeof(int) );
				N[i].child[N[i].chdLen-1] = t;
				N[t].parent = i;
			}
		}
		for(i = 1;i <= n;i++){
			N[i].color = 0;
			N[i].from = -1;
			N[i].d = n+1;
		}
		for(i = 1;i <= n;i++){
			if(N[i].parent == -2)r = i;
		}
		BFS(r);
		for(i = 1;i <= n;i++){
			if(N[i].chdLen == 0)N[i].T = 0;
			else N[i].T = -100;
		}
		l = 0;
		for(i = 1;i <= n;i++){
			if(N[i].chdLen == 0){
				l++;
				leaf = realloc(leaf,l * sizeof(struct iNd));
				leaf[l-1].ind = i;
				leaf[l-1].d = N[i].d;
			}
		}
		qsort(leaf,l,sizeof(struct iNd),CMP);
		for(i = 0;i < l;i++){
			c = 0;
			a = leaf[i].ind;
			ad = leaf[i].d;
			f = N[a].from;
			//for(j = 0;j < N[a].d;j++){
			while(f!=-1){
				if(N[f].T == -100){
					c++;
					N[f].T = c; 
				}
				else break;
				f = N[f].from;
			}
		}
		ans = 0;
		for(i = 1;i <= n;i++) ans += (long long) (N[i].T);	//ans += N[i].T;
		printf("%d\n",r);
	//	printf("%d\n",ans);
		printf("%lld\n", ans);
	}
	return 0;
}

int CMP(const void* a,const void* b){
	struct iNd *A = (struct iNd*) a;
	struct iNd *B = (struct iNd*) b;
	if(A[0].d < B[0].d)return 1;
	else if(A[0].d == B[0].d)return 0;
	else return -1;
}

void BFS(int n){
	int p,i,t;
	N[n].color = 1;
	enqueue(n);
	N[n].d = 0;
	while(empty != 1){
		p = dequeue();
		for(i = 0;i < N[p].chdLen;i++){
			t = N[p].child[i];
			if(N[t].color == 0){
				N[t].color = 1;
				enqueue(t);
				N[t].from = p;
				N[t].d = N[p].d+1;
			}
			N[p].color = 2;
		}
	}
}

void Height(int a,int n){
	int i,j,t,tans;
	for(i = 1;i <= n;i++){
		if(N[i].chdLen == 0){
			t = N[i].from;
			for(j = 0;j < N[i].d;j++){
				if(t == a){
					tans = N[i].d - N[a].d;
					if(tans > N[a].T)N[a].T = tans;
				}
				else t = N[t].from;
			}
		}
	}
}

void printChild(int n){
	int i;
	for(i = 0;i < N[n].chdLen;i++){
		printf("%d.%d ",n,N[n].child[i]);
	}
	printf("\n");
}

void printParent(int n){
	int i;
		printf("%d %d",n,N[n].parent);
	printf("\n");
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
