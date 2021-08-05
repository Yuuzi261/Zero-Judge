def main():
    while True:
        try:
            hh, mm = input().split()
        except:
            break

        hh, mm = int(hh), int(mm)
        mins = hh * 60 + mm

        if 450 <= mins < 1020:
            print('At School')
        else:
            print('Off School')

main()
