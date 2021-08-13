def main():
    N = [1, 2]
    for i in range(2, 100):
        N.append(N[i - 2] + N[i - 1])
    while True:
        try:
            n = int(input())
        except:
            break

        print(N[n - 1])

main()
