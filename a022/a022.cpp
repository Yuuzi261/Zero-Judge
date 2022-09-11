//py的解法太混了補一個別的方法
#include <iostream>
#include <string.h>
using namespace std;

bool isPalindrome(char *x) {
    char y[1001];
    int i = 0, j = 0;
    while(x[i] != '\0')
        i++;
    i--;
    while(i >= 0){
    	y[j] = x[i];
    	i--;
        j++;
    }
    y[j] = '\0'; //可有可無
    if (strcmp(x, y) == 0)
        return 1;
    else
        return 0;
}

int main() {
    char n[1001];
    while(scanf("%s", &n) != EOF){
        if(isPalindrome(n))
        	cout << "yes" << endl;
        else
        	cout << "no" << endl;
    }

    return 0;
}
