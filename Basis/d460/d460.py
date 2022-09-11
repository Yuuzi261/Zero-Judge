def main():
    while True:
        try:
            y = int(input())
        except:
            break

        print((y > 5) * 590 + (y > 11) * 200 + (y > 17) * 100 - (y > 59) * 491)

main()
