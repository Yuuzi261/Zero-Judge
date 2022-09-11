def main():
    while True:
        try:
            n = int(input())
        except:
            break

        for i in range(1, 2 * n, 2):
            print('_' * ((2 * n - i - 1) // 2) + '*' * i + '_' * ((2 * n - i - 1) // 2))

main()
