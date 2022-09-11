def main():
    while True:
        try:
            n = int(input())
        except:
            break

        while n >= 3:
            if n >= 900000000:
                n -= 900000000
            elif n >= 90000000:
                n -= 90000000
            elif n >= 9000000:
                n -= 9000000
            elif n >= 900000:
                n -= 900000
            elif n >= 90000:
                n -= 90000
            elif n >= 9000:
                n -= 9000
            elif n >= 900:
                n -= 900
            elif n >= 90:
                n -= 90
            elif n >= 9:
                n -= 9
            elif n >= 3:
                n -= 3

        if n == 0:
            print('YES')
        else:
            print('NO')

main()
