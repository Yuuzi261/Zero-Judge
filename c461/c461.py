def main():
    while True:
        try:
            L = input().split()
        except:
            break

    
        for i in range(3):
            if int(L[i]) == 0:
                L[i] = False
            else:
                L[i] = True

        ans = []
        
        if (L[0] and L[1]) == L[2]:
            ans.append('AND')
        if (L[0] or L[1]) == L[2]:
            ans.append('OR')
        if (L[0] ^ L[1]) == L[2]:
            ans.append('XOR')

        if ans != []:
            for x in ans:
                print(x)
        else:
            print('IMPOSSIBLE')


main()
