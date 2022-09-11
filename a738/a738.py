def main():
    while True:
        try:
            i, j = input().split()
        except:
            break
        
        i, j = int(i), int(j)
        
        while (i % j) != 0:
            k = i % j
            i = j
            j = k
            
        print(j)
        
main()
