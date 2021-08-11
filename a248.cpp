#include <iostream>

using namespace std;

int main(){
    int a, b, N, remainder, i, L[10001];
    while(scanf("%d %d %d", &a, &b, &N) != EOF){
        L[0] = a / b;
        remainder = a % b * 10;
        for(i = 1;i < N + 1;i++){
            L[i] = remainder / b;
            remainder = remainder % b * 10;
        }
        cout << L[0] << '.';
        for(i = 1;i < N + 1;i++)
            cout << L[i];
        cout << endl;
    }
    return 0;
}
