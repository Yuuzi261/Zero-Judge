#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, m, k, i, now;
    while(scanf("%d",&n) != EOF){
        scanf("%d %d",&m, &k);
        int tempL[n];
        for(i = 0;i < n;i++){
            tempL[i] = i+1;
        }
        vector<int> people(tempL,tempL+n);

        now = 0;
        for(i = 0;i < k;i++){
            now += (m-1);
            now%=n;
            people.erase(people.begin() + now);
            n-=1;
        }
        printf("%d\n",people[now%n]);
    }
    return 0;
}