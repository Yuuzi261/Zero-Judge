while True:
    try:
        a = input()
        b = a[::-1]
        if a==b:
            print('yes')
        else:
            print('no')
    except:
        break
