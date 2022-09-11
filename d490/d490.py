def main():
    while True:
        try:
            a, b = input().split()
            a, b = int(a), int(b)
        except:
            break

        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b -= 1

        print((a + b) * ((b - a) // 2 + 1) // 2)

main()
