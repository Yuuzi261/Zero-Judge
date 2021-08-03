def main():
    while True:
        try:
            N = input().split(' ')
        except:
            break

        N = N[1:len(N)]
        
        i = 1
        hilltop = 0
        while True:
            if i < len(N)-1:
                if int(N[i-1]) < int(N[i]) and int(N[i]) > int(N[i+1]):
                    hilltop += 1
                elif int(N[i-1]) < int(N[i]) == int(N[i+1]):
                    temp = int(N[i])
                    while temp == int(N[i]):
                        if i < len(N)-1:
                            i += 1
                        else:
                            break
                    if int(N[i]) < temp:
                        hilltop += 1
                i += 1
            else:
                break

        print(hilltop)


main()
