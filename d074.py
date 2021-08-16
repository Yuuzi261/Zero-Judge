def main():
    while True:
        try:
            n = int(input())
        except:
            break

        L = input().split()

        Max = -1

        for x in L:
            if int(x) > Max:
                Max = int(x)

        print(Max)

main()
