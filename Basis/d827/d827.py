def main():
    while True:
        try:
            N = int(input())
        except:
            break

        print(N // 12 * 50 + N % 12 * 5)

main()
