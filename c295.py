MaxNumbers = []

def FindMaxNumber(i, Numbers):
    maxNum = 0
    global MaxNumbers
    for x in Numbers[i]:
        if int(x) > maxNum:
            maxNum = int(x)

    MaxNumbers.append(maxNum)

    return maxNum

def main():
    while True:
        try:
            N, M = input().split()
            N, M = int(N), int(M)
        except:
            break
        
        global MaxNumbers
        Numbers = []
        for i in range(N):
            Numbers.append(input().split(" "))

        S = 0
        for i in range(N):
            S += FindMaxNumber(i, Numbers)

        ans = []
        for x in MaxNumbers:
            if S % x == 0:
                ans.append(x)

        print(S)
        if ans != []:
            for i in range(len(ans)):
                if i != len(ans)-1:
                    print(ans[i], end = ' ')
                else:
                    print(ans[i], end = '')
        else:
            print(-1, end = '')
        print()

        MaxNumbers.clear()

main()
