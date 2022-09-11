def main():
    while True:
        try:
            N = input()
        except:
            break

        if N[0] == '-':
            N = N[1:]
        Sum = 0
        for x in N:
            Sum += int(x)

        if not(Sum%3):
            print('yes')
        else:
            print('no')

main()
