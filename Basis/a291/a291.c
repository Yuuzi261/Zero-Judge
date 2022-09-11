#include <stdio.h>
#include <stdlib.h>

void check(int*, int*, int*, int*);

int main(void) {

    int n, i, A, B;
    int pwd[4], input_pwd[4];

    while(scanf("%d %d %d %d", &pwd[0], &pwd[1], &pwd[2], &pwd[3]) != EOF) {

        scanf("%d", &n);

        for(i = 0;i < n;i++) {

            A = 0, B = 0;
            scanf("%d %d %d %d", &input_pwd[0], &input_pwd[1], &input_pwd[2], &input_pwd[3]);
            check(pwd, input_pwd, &A, &B);
            printf("%dA%dB\n", A, B);

        }

    }

    return 0;

}

void check(int pwd[], int input_pwd[], int* A, int* B) {

    int i;
    int val[10];

    for(i = 0;i < 10;i++)
        val[i] = 0;

    for(i = 0;i < 4;i++)
        val[pwd[i]]++;

    for(i = 0;i < 4;i++) {
        if(val[input_pwd[i]] > 0 && input_pwd[i] == pwd[i]) {
            *A += 1;
            val[input_pwd[i]]--;
        }
    }

    for(i = 0;i < 4;i++) {
        if(val[input_pwd[i]] > 0 && input_pwd[i] != pwd[i]) {
            *B += 1;
            val[input_pwd[i]]--;
        }
    }

}
