def main():
    while True:
        try:
            t1, t2, t3, x1, x3 = input().split()
        except:
            break
        
        t1, t2, t3, x1, x3 = float(t1), float(t2), float(t3), float(x1), float(x3)
        x2 = ((t2-t3)/(t1-t3))*(x1-x3)+x3
        
        print('%f' %x2)
    
main()
