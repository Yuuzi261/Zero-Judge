def main():
    t = int(input())
    
    for i in range(t):
        S = list(map(int, input().split()))
        if(S[1] - S[0] == S[2] - S[1]):
            S.append(S[3] + (S[1] - S[0]))
        else:
            S.append(int(S[3] * (S[1] / S[0])))
            
        [print(x, end = ' ') for x in S]
        print()
    
    
main()
