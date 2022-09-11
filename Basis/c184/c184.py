def allFactorSum(n: int):
    factorSum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factorSum += i + n // i
            
    return factorSum

def main():
    while True:
            
        n = int(input())
        if n == 0:
            break
        
        factorSum = allFactorSum(n)
        
        if factorSum == n:
            print(f"={n}")
        else:
            if allFactorSum(factorSum) == n:
                print(factorSum)
            else:
                print(0)
    
    
main()
