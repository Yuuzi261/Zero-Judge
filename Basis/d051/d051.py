def main():
    while True:
        try:
            a = int(input())
        except:
            break
    
        ans = (a-32)*5/9
        
        print('%.3f' %ans)
    
main()
