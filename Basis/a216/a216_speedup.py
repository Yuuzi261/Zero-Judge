fL = [1]
gL = [1]
fn = 1
gn = 1

def f(n):
    global fL
    global fn
    if(n > fn):
        sum = fL[-1]
        for i in range(fn + 1, n + 1):
            sum += i
            fL.append(sum)
        fn = n

def g(n):
    global fL
    global gL
    global gn
    if(n > gn):
        sum = gL[-1]
        for i in range(gn, n):
            sum += fL[i]
            gL.append(sum)
        gn = n

def main():
    global fL
    global gL
    while True:
        try:
            n = int(input())
        except:
            break

        f(n), g(n)
        print(fL[n-1], gL[n-1])


main()
