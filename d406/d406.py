import queue

class node:
    def __init__(self, color, x, y):
        self.color = color
        self.time = 0
        self.coordinate = [x, y]

def BFS(Nodes, s, n, m):
    q = queue.Queue()
    for x in Nodes[0]:
        if x.color == 1:
            x.color = 2
            x.time = 1
            q.put(x)
            break
    
    coordinate = []
    while not(q.empty()):
        currentN = q.get()
        coordinate = currentN.coordinate
        if 0 <= coordinate[0] + 1 < n: #water tries to flow down
            coordinate[0] += 1
            nextN = Nodes[coordinate[0]][coordinate[1]]
            if nextN.color == 1:
                nextN.color = 2
                nextN.time = currentN.time + 1
                q.put(nextN)
            coordinate[0] -= 1
        if 0 <= coordinate[1] - 1 < m: #water tries to flow to the left
            coordinate[1] -= 1
            nextN = Nodes[coordinate[0]][coordinate[1]]
            if nextN.color == 1:
                nextN.color = 2
                nextN.time = currentN.time + 1
                q.put(nextN)
            coordinate[1] += 1
        if 0 <= coordinate[1] + 1 < m: #water tries to flow to the right
            coordinate[1] += 1
            nextN = Nodes[coordinate[0]][coordinate[1]]
            if nextN.color == 1:
                nextN.color = 2
                nextN.time = currentN.time + 1
                q.put(nextN)
            coordinate[1] -= 1
        if s == 1:
            if 0 <= coordinate[0] - 1 < n: #water tries to flow up
                coordinate[0] -= 1
                nextN = Nodes[coordinate[0]][coordinate[1]]
                if nextN.color == 1:
                    nextN.color = 2
                    nextN.time = currentN.time + 1
                    q.put(nextN)
                coordinate[0] += 1

        currentN.color = 0
    
    return Nodes

def main():
    count = 1
    while True:
        try:
            s = int(input())
        except:
            break

        n, m = input().split()
        n, m = int(n), int(m)

        Nodes = []
        for i in range(n):
            tempL = input().split(' ')
            tempN = []
            for j in range(m):
                tempN.append(node(int(tempL[j]), i, j))
            Nodes.append(tempN)

        Nodes = BFS(Nodes, s, n, m)

        print(f'Case {count}:')
        for i in range(n):
            for j in range(m):
                print(f'{Nodes[i][j].time} ', end = '')
            print()
        count += 1

main()
