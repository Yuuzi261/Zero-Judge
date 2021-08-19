P = []
n = -1

def PaintBucket(x, y):
    P[x][y] = '+'
    if 0 <= x - 1 < n:
        if P[x - 1][y] == '-':
            PaintBucket(x - 1, y)
    if 0 <= x + 1 < n:
        if P[x + 1][y] == '-':
            PaintBucket(x + 1, y)
    if 0 <= y - 1 < n:
        if P[x][y - 1] == '-':
            PaintBucket(x, y - 1)
    if 0 <= y + 1 < n:
        if P[x][y + 1] == '-':
            PaintBucket(x, y + 1)
    

def main():
    while True:
        try:
            global n
            n = int(input())
        except:
            break

        global P
        for i in range(n):
            t = input()
            T = []
            for x in t:
                T.append(x)
            P.append(T)

        x, y = input().split()
        PaintBucket(int(x), int(y))

        for i in range(n):
            for j in range(n):
                print(P[i][j], end = '')
            print()

        P.clear()

main()
