def main():
    while True:
        try:
            n = int(input())
        except:
            break

        if n == 0:
            break

        for i in range(n):
            if i%7 != 0:
                print(i,end = ' ')
        print()


main()
