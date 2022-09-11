def main():
    while True:
        try:
            a, b = input().split()
        except:
            break
        
        a, b = int(a),int(b)
        
        if a <= b:
            print(b-a)
        else:
            print(100-a+b)
    
main()
