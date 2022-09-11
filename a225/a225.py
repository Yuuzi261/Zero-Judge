def main():
    while True:
        try:
            n = int(input())
        except:
            break

        L = []
        L = input().split()

        NumList = [[], [], [], [], [], [], [], [], [], []]

        for x in L:
            NumList[int(x) % 10].append(int(x))

        for x in NumList:
            x.sort(reverse = True)

        for x in NumList:
            for y in x:
                print(y, '', end = '')
        print()

main()
