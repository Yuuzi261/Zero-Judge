def main():
    while True:
        try:
            N = input().split()
        except:
            break

        for i in range(len(N)):
            N[i] = int(N[i])

        ans = 0
        for x in N:
            ans += x

        print(ans)

main()
