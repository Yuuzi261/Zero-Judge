def rotate(matrix: list):
    L = []
    lenOfRow = len(matrix[0])
    numOfRow = len(matrix)
    
    for i in range(lenOfRow):
        L.append([])
       
    for j in range(lenOfRow-1, -1, -1): 
        for i in range(numOfRow):
            L[lenOfRow-j-1].append(matrix[i][j])
            
    return L

def printMatrix(matrix: list):
    print(f"{len(matrix)} {len(matrix[0])}")
    for row in matrix:
        for number in row:
            print(number, end = ' ')
        print()

def main():
    while True:
        try:
            R, C, M = map(int, input().split())
        except:
            break
        
        matrix = []
        for i in range(R):
            matrix.append(list(map(int, input().split())))
            
        cmdList = list(map(int, input().split()))
        
        for cmd in cmdList[::-1]:
            if cmd == 0:
                matrix = rotate(matrix)
            else:
                matrix.reverse()
                
        printMatrix(matrix)
    
    
main()
