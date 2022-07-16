from functools import cmp_to_key
    
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
        items = list(zip(w, f))
        items.sort(key=cmp_to_key(lambda x,y: x[0] * y[1] - x[1] * y[0]))
        printEnergy(items)
    
    
main()
