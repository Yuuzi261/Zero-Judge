def main():
    while True:
        try:
            n = int(input())
        except:
            break

        print((n + 1) * n // 2)

main()
