class People:
    def __init__(self, friend):
        self.friend = friend
        self.color = 0

def group(P):
    count = 0
    for i in range(len(P)):
        temp = i
        if P[temp].color == 0:
            count += 1
        while P[temp].color == 0:
            P[temp].color = -1
            temp = P[temp].friend

    return count
        
def main():
    while True:
        try:
            N = int(input())
        except:
            break

        Friend_List = input().split(" ")
        P = []
        for x in Friend_List:
            P.append(People(int(x)))

        print(group(P))

main()
