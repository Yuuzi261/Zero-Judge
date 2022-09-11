def main():
    L = [0, 5, 8, 8, 2, 3, 5, 2, 9, 4, 1, 1, 7, 6, 4, 7]
    while True:
        try:
            m = int(input())
        except:
            break

        for i in range(m):
            n = int(input())
            Sum = n // 16 * 72
            for j in range(n % 16):
                Sum += L[j]

            print(L[n%16 - 1], Sum)

main()
