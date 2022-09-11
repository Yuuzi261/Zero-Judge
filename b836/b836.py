def main():
    while True:
        try:
            n, m = input().split()
        except:
            break
        
        n, m = int(n), int(m)
        
        if m != 0:
            judge = (n-1)%m
        else:
            judge = 0

        if judge == 0:
            print('Go Kevin!!')
        else:
            print('No Stop!!')
          
main()
