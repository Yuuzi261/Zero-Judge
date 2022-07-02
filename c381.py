def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        document = ""
        for i in range(n):
            document += input()
            
        pwd = list(map(int, input().split()))
        decode = ""
        
        for x in pwd:
            decode += document[x - 1]
            
        print(decode)
    
    
main()
