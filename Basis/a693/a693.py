def main():
    while True:
        try:
            n, m = input().split()
        except:
            break

        n, m = int(n), int(m)

        FoodList = input().split()
        SumList = [0]
        Sum = 0
        for x in FoodList:
            Sum += int(x)
            SumList.append(Sum)

        for i in range(m):
            l, r = input().split()
            l, r = int(l) - 1, int(r)
            print(SumList[r] - SumList[l])

main()
