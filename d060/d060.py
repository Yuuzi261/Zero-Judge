def main():
    while True:
        try:
            m = int(input())
        except:
            break

        print((85-m)%60)

main()
