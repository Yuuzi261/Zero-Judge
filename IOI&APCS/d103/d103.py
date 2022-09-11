def calIdentifier(ISBN: list):
    identifier = 0
    for i in range(len(ISBN) - 1):
        identifier += int(ISBN[i]) * (i + 1)
    identifier %= 11
    
    if identifier != 10:
        return str(identifier)
    else:
        return 'X'
    
def printISBN(ISBN: list, identifier: str):
    ISBN.pop(), ISBN.append(identifier)
    ISBN.insert(1, '-'), ISBN.insert(5, '-'), ISBN.insert(11, '-')
    for x in ISBN:
        print(x, end = '')

def main():
    while True:
        try:
            input_data = input().replace('-', '')
        except:
            break
        
        ISBN = [number for number in input_data]
        identifier = calIdentifier(ISBN)
        
        #because of the stupid test data, if no input, continue.
        try:
            if identifier == ISBN[9]:
                print("Right")
            else:
                printISBN(ISBN, identifier)
        except:
            continue
        
    
main()
