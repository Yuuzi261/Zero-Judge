def main():
    while True:
        try:
            P = input().split()
        except:
            break
        
        L = ['A', 'B', 'C']
        for i in range(3):
            P[i] = int(P[i])

        for i in range(2):
            for j in range(2):
                if P[j] > P[j+1]:
                    temp = P[j]
                    P[j] = P[j+1]
                    P[j+1] = temp
                    temp = L[j]
                    L[j] = L[j+1]
                    L[j+1] = temp

        if P[0] + P[1] > P[2]:
            print(L[1])
        else:
            print(L[2])

main()
