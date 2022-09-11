def coin(X: int, a: int, b: int):
    mnSum = 3000 # 1000 >= X >= a >= b >= 1, set mnSum is a large enough number
    m, n = 0, 0
    while m * a <= X:
        if (X - m * a) % b == 0:
            n = (X - m * a) // b
            if m + n <= mnSum:
                mnSum = m + n
                
        m += 1
        
    if mnSum != 3000:
        return mnSum
    else:
        return -1
            

def main():
    while True:
        try:
            N = int(input())
        except:
            break
        
        for i in range(N):
            X, a, b = map(int, input().split())
            print(coin(X, a, b))
    
    
main()
