def main():
    while True:
        try:
            a = float(input())
        except:
            break
    
        ans = a/(abs(a)-0.1)
        print(int(ans))
    
main()
