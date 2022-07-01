def main():
    while True:
        try:
            n = int(input())
        except:
            break
        
        for i in range(n // 7):
            for j in range(1, 7):
                print(j + 7 * i, end = ' ')
                
        for i in range(n - n % 7 + 1, n):
            print(i, end = ' ')
            
        print()
            
        
main()
