def main():
    while True:
        try:
            N = int(input())
        except:
            break

        print((N - 1) // 3 + 1)

main()
