def qsort(L:list, i: int, j: int):
    if j <= i: return
    start, end = i, j
    while i != j:
        while (L[start][0] * L[j][1] <= L[j][0] * L[start][1]) and (j > i): j -= 1
        while (L[start][0] * L[i][1] >= L[i][0] * L[start][1]) and (i < j): i += 1
        L[i], L[j] = L[j], L[i]

    L[start], L[i] = L[i], L[start]
    qsort(L, start, i - 1), qsort(L, i + 1, end)
    
def printEnergy(L: list):
    energy, weight = 0, 0
    for i in range(1, len(L)):
        weight += L[i - 1][0]
        energy += weight * L[i][1]
        
    print(energy)

def main():
    while True:
        try:
            N = int(input())
        except:
            break
        
        w = list(map(int, input().split()))
        f = list(map(int, input().split()))
        items = [[x, y]for x, y in zip(w, f)]
        qsort(items, 0, len(items) - 1)
        printEnergy(items)
    
    
main()
