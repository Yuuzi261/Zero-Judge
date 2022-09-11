def f(n, L):
    sum = 0
    for i in range(1, n+1):
        sum += i
        L.append(sum)

    return sum, L

def g(n, L):
    sum = 0
    for x in L:
        sum += x

    return sum

def main():
    while True:
        try:
            n = int(input())
        except:
            break

        L = []
        L = f(n, L)[1]
        ans = g(n, L)
        print(L[n-1], ans)


main()
