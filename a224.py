def main():
    while True:
        try:
            a = input()
        except:
            break

        L = []
        aL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for x in a:
            if x.isalpha():
                x = x.lower()
                L.append(x)

        oddt = 0

        for x in aL:
            c = 0
            for y in L:
                if x == y:
                    c+=1
            if c%2 != 0:
                oddt += 1
            
        

        if oddt <= 1:
            print('yes !')
        else:
            print('no...')


main()
