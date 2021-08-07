def main():
    while True:
        try:
            s = input()
        except:
            break

        for x in s:
            if not(x.isalpha()):
                s = s.replace(x, ' ')

        L = s.split()
        print(len(L))

main()
