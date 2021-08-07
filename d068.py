def main():
    while True:
        try:
            w = int(input())
        except:
            break

        if w > 50:
            print(w-1)
        else:
            print(w)

main()
