def main():
    while True:
        try:
            a, b, c, d, e, f = map(int, input().split())
        except:
            break
        
        deltaX = c * e - b * f
        deltaY = a * f - c * d
        delta = a * e - b * d
        
        if deltaX == 0 and deltaY == 0 and delta == 0:
            print("Too many")
        elif delta == 0 and (deltaX != 0 or deltaY != 0):
            print("No answer")
        else:
            print(f"x={'%.2f' % (deltaX / delta)}")
            print(f"y={'%.2f' % (deltaY / delta)}")
    
    
main()
