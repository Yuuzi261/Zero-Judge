def main():
    while True:
        try:
            n, k = input().split()
        except:
            break

        N = input().split()
        L = input().split()

        for i in range(len(N)):
            N[i] = int(N[i])

        for i in range(len(L)):
            L[i] = int(L[i])

        for x in L:
            isFind = False
            l, r = 0, int(n) - 1
            while l <= r:
                m = (l + r) // 2
                if N[m] > x:
                    r = m - 1
                elif N[m] < x:
                    l = m + 1
                else:
                    print(m + 1)
                    isFind = True
                    break

            if not(isFind):
                print(0)     

main()
