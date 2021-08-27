def main():
    while True:
        try:
            n, k = input().split()
            n, k = int(n), int(k)
        except:
            break

        isPossible = True

        if k != 0:
            if n % k != 0:
                isPossible = False
        else:
            if n != 0:
                isPossible = False

        if isPossible:
            print('Ok!')
        else:
            print('Impossib1e!')

main()
