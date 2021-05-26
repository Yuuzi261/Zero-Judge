def main():
    while True:
        L = []
        try:
            a = int(input())
            L.append(a)
        except:
            break
        
        while True:
            try:
                a = int(input())
                L.append(a)
            except:
                break

        L.reverse()

        t = L[0]
        ans = []
        count = 1

        for i in range(t):
            n = L[count]
            sum = 0

            for j in range(n):
                sum += L[count+1+j]

            ans.append(sum)
            count += (L[count]+1)

        ans.reverse()
        for x in ans:
            print(x)


main()
