def main():
    while True:
        try:
            n = int(input())
        except:
            break
        
        print(n*n-n+2)
          
main()
