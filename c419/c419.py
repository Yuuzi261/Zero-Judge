def main():
    while True:
        try:
            n = int(input())
        except:
            break

        for i in range(n):
            print('_' * (n - i - 1) + '*' * (i + 1))

main()
