def main():
    while True:
        try:
            n, m = input().split()
            n, m = int(n), int(m)
        except:
            break

        for i in range(n):
            PanN = input().split()
            FlowerN = input().split()
            setP = set()
            setF = set()
            for x in PanN:
                setP.add(int(x))
            for x in FlowerN:
                setF.add(int(x))

            print(len(setP & setF))

main()
