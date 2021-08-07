#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isPrimeNumber(int n){
    if(n == 2 || n == 3)
        return 1;
    else if(n > 4){
        int m = n % 6;

        if(m != 1 && m != 5){
            return 0;
        }

        int nSqrt = floor(sqrt(n));

        for(int i = 5; i <= nSqrt; i += 6){
            if(n % i == 0 || n % (i + 2) == 0){
                return 0;
            }
        }

        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        if(isPrimeNumber(n))
            printf("質數\n");
        else
            printf("非質數\n");

    }

    return 0;
}
