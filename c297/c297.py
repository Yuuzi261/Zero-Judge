hitsDict = {'1B': 1, '2B': 2, '3B': 3, 'HR': 4}

def Hit(field: list, outs: int, record: str):
    global hitsDict
    if record == '1B' or record == '2B' or record == '3B' or record == 'HR':
        for i in range(len(field)):
            field[i] += hitsDict[record]
        field.append(hitsDict[record])
    else:
        outs += 1
        
    return outs

def checkField(field: list):
    score = 0
    for i in range(len(field)-1, -1, -1):
        if field[i] >= 4:
            score += 1
            field.remove(field[i])
            
    return score

def convertTo1D(origin: list):
    for i in range(len(origin)):
        origin[i].pop(0)
    
    Record = []
    
    while origin != []:
        for L in origin:
            Record.append(L[0])
            L.pop(0)
        while True:
            try:
                origin.remove([])
            except:
                break
                
    return Record

def startGame(Record: list, outLimit: int):
    score, outs = 0, 0
    field = []
    
    for record in Record:
        outs = Hit(field, outs, record)
        if outs >= outLimit:
            break
        elif outs == 3:
            field.clear()
            outs = 0
            outLimit -= 3
            
        score += checkField(field)
        
    return score
    

def main():
    while True:
        try:
            input_data = [list(input().split()) for i in range(9)]
        except:
            break
        
        outLimit = int(input())
        Record = convertTo1D(input_data)
        print(startGame(Record, outLimit))
    
    
main()
