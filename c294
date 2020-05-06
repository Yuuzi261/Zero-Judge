def main():
    while True:
        try:
            a, b, c = input().split()
        except:
            break
    
        a, b, c = int(a), int(b), int(c)
    
        L = [a, b, c]
        L = sorted(L)
        
        print(L[0],L[1],L[2])
    
        if L[0]+L[1] <= L[2]:
            print('No')
        elif L[0]**2 + L[1]**2 < L[2]**2:
            print('Obtuse')
        elif L[0]**2 + L[1]**2 == L[2]**2:
            print('Right')
        else:
            print('Acute')

main()
