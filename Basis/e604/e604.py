def main():
    while True:
        try:
            n = int(input())
        except:
            break

        print(2 * 3 ** n - 1)

main()
