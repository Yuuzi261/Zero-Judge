def printDict(numDict: dict):
    for numList in numDict.values():
        if numList != []:
            print(*numList, end = ' ')
    print()

def main():
    while True:
        try:
            n = int(input())
        except:
            break

        inputList = input().split()

        numDict = {str(i):[] for i in range(10)}
        
        for number in inputList:
            numDict[number[-1]].append(int(number))
            
        for value in numDict.values():
            value.sort(reverse=True)
            
        printDict(numDict)


main()
