def rotate(matrix: list):
    lenOfRow = len(matrix[0])
    numOfRow = len(matrix)
    
    L = [[matrix[i][j] for i in range(numOfRow)] for j in range(lenOfRow-1, -1, -1)]
            
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
        
        matrix = [list(map(int, input().split())) for i in range(R)]
        cmdList = list(map(int, input().split()))
        
        for cmd in cmdList[::-1]:
            if cmd == 0:
                matrix = rotate(matrix)
            else:
                matrix.reverse()
                
        printMatrix(matrix)
    
    
main()
