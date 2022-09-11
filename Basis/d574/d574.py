def main():
    while True:
        try:
            n = input()
        except:
            break

        try:
            n = int(n)
            S = input()
        except:
            for i in range(len(n)):
                if n[i].isalpha():
                    break
            S = n[i:]
            n = int(n[:i])

        S += ' '
        now = S[0]
        NewS = ''
        i = 0

        for x in S:
            if x == now:
                i += 1
            else:
                NewS += str(i) + now
                now = x
                i = 1

        if len(NewS) < len(S[:len(S)-1]):
            print(NewS)
        else:
            print(S[:len(S)-1])

main()
