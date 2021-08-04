#include <iostream>

using namespace std;

int main(){
    int n, i, j, k = 1, hilltop = 0, temp, previous;
    int L[10001];
    while(scanf("%d", &n) != EOF){
        j = 0, previous = -1;
        for(i = 0; i < n; i++){
            scanf("%d", &temp);
            if(previous == temp)
                continue;
            else{
                L[j] = temp;
                j++;
            }
            previous = temp;
        }
        while(1){
            if(k < j-1){
                if(L[k-1] < L[k] && L[k] > L[k+1])
                    hilltop++;
                k++;
            }
            else
                break;
        }

        cout << hilltop << endl;
        k = 1;
        hilltop = 0;


    }
    return 0;
}
