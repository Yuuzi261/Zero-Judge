#include <iostream>
#include <unordered_set>

using namespace std;

int main(){
    int N, i, j, t1, t2;
    unordered_set<int> NS;
    while(scanf("%d", &N) != EOF){
        for(i = 0;i < N;i++){
            scanf("%d %d", &t1, &t2);
            if(t1 != t2){
                for(j = t1;j < t2;j++)
                    NS.insert(j);
            }
        }
        cout << NS.size() << endl;
        NS.clear();
    }
    return 0;
}
