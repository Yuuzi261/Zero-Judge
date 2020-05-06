#include <iostream>

using namespace std;

struct people{
    int hand;
    int color;
};

void circle(struct people* p,int now);
void printArr(struct people* p,int n);

int cot;

int main(void){
    int n, t, i;
    while((scanf("%d",&n)) != EOF){
        struct people p[n];
        cot = 0;
        for(i = 0;i < n;i++){
            p[i].color = 0;
        }
        for(i = 0;i < n;i++){
            cin >> t;
            p[i].hand = t;
        }
        for(i = 0;i < n;i++){
            if(p[i].color != 1)
                circle(p,i);
        }
        cout << cot << endl;
    }

    return 0;
}

void circle(struct people* p,int now){
    int color = 0;
    while(color != 1){
        if(p[now].hand != now){
            if(p[now].color != 1){
                p[now].color = 1;
                now = p[now].hand;
            }
            else{
                color = 1;
            }
        }
        else{
            p[now].color = 1;
            color = 1;
        }
    }
    cot++;
}

void printArr(struct people* p,int n){
    int i;
    for(i = 0;i < n;i++){
        cout << ' ' << p[i].hand << ' ' << p[i].color << endl;
    }
}
