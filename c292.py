def move(N, direction, Colors, Coordinate):
    while True:
        if direction == 0:
            Coordinate[1] -= 1
            direction = 1
        elif direction == 1:
            Coordinate[0] -= 1
            direction = 2
        elif direction == 2:
            Coordinate[1] += 1
            direction = 3
        else:
            Coordinate[0] += 1
            direction = 0

        if 0 <= Coordinate[0] <= N-1 and 0 <= Coordinate[1] <= N-1:
            if Colors[Coordinate[0]][Coordinate[1]] == -1:
                if direction == 0:
                    Coordinate[0] -= 1
                    direction = 2
                elif direction == 1:
                    Coordinate[1] += 1
                    direction = 3
                elif direction == 2:
                    Coordinate[0] += 1
                    direction = 0
                else:
                    Coordinate[1] -= 1
                    direction = 1
            else:
                break
        else:
            break
            

    return Coordinate, direction

def tornado(N, direction, Numbers, Colors, Coordinate):
    ans = ''
    while 0 <= Coordinate[0] <= N-1 and 0 <= Coordinate[1] <= N-1:
        Colors[Coordinate[0]][Coordinate[1]] = -1
        ans += str(Numbers[Coordinate[0]][Coordinate[1]])
        temp = move(N, direction, Colors, Coordinate)
        Coordinate = temp[0]
        direction = temp[1]

    return ans

def main():
    while True:
        try:
            N = int(input())
        except:
            break

        direction = int(input())
        Numbers = []
        Colors = []
        for i in range(N):
            tempL = input().split(" ")
            Numbers.append(tempL)
            Colors.append([0]*N)
        
        Coordinate = [N//2, N//2]
        print(tornado(N, direction, Numbers, Colors, Coordinate))


main()
