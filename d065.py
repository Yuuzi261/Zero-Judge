def main():
    while True:
        try:
            L = input().split()
        except:
            break

        for i in range(3):
            L[i] = int(L[i])

        L.sort()

        print(L[2])

main()
