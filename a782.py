def main():
    while True:
        try:
            S = input().split(" ")
            if S[0] == "END":
                break
        except:
            break
        
        RAS = ''
        for x in S:
            RAS += x[0].upper()

        RAS += ' ' + S[len(S) - 1]

        print(RAS)

main()
