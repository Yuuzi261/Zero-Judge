def main():
    while True:
        try:
            N = int(input())
        except:
            break
        
        Lines = [list(map(int, input().split())) for _ in range(N)]
        Lines.sort()
        
        length = 0
        start, end = Lines[0][0], Lines[0][1]
        for l in Lines[1:]:
            if l[0] >= end:
                length += end - start
                start, end = l[0], l[1]
            elif l[1] > end:
                end = l[1]
        
        length += end - start    
        print(length)
            
    
main()
