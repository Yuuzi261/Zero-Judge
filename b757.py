def main():
    while True:
        try:
            r = float(input())
        except:
            break

        R = (r * 9) / 5 + 32

        print("%g"%(R))

main()
