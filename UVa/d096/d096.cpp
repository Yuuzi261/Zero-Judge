#include<iostream>
#include<math.h>

using namespace std;

int main() {
    
    unsigned long long n;
    
    while(cin >> n)
        cout << (3 * n * n + 6 * n + 3) / 2 - 9 << endl;

    return 0;
}