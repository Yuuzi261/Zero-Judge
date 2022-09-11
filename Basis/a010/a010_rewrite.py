def main():
    while True:
        try:
            number = int(input())
        except:
            break
        
        power = 0
        factor = 2
        
        while number != 1:
            while number % factor == 0:
                number /= factor
                power += 1
                
            if power == 1:
                print(factor, end = '')
            elif power > 1:
                print(f"{factor}^{power}", end = '')
                
            if number != 1 and power != 0:
                print(" * ", end = '')
                
            factor += 1
            power = 0
            
        print()
    
    
main()
