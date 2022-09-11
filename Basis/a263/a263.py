import datetime

def main():
    while True:
        try:
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))
        except:
            break
        
        print(abs((datetime.datetime(a[0], a[1], a[2]) - datetime.datetime(b[0], b[1], b[2])).days))
    
    
main()
