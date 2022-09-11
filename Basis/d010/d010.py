def main():
    while True:
        try:
            n = int(input())
        except:
            break

        L = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                L.append(i)

        S = 0
        for x in L:
            S += x

        if S > n:
            print('盈數')
        elif S < n:
            print('虧數')
        else:
            print('完全數')

main()
