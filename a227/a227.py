def hanoi(n, A, B, C):
    if n == 1:
        print(f'Move ring {n} from {A} to {C}')
    else:
        hanoi(n - 1, A, C, B)
        print(f'Move ring {n} from {A} to {C}')
        hanoi(n - 1, B, A, C)

def main():
    while True:
        try:
            N = int(input())
        except:
            break

        hanoi(N, 'A', 'B', 'C')

main()
