def main():
    while True:
        try:
            Stones = input().split()
        except:
            break

        N = []
        T = []

        for x in Stones:
            if int(x) in N:
                T[N.index(int(x))] += 1
            else:
                N.append(int(x))
                T.append(1)

        for i in range(len(T)):
            if T[i] % 3 != 0:
                print(N[i])

main()
