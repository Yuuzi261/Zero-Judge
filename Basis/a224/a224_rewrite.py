def main():
    while True:
        try:
            origin = input()
        except:
            break
        
        L = [x.lower() for x in origin if x.isalpha()]
        alphaDict = {chr(_):0 for _ in range(97, 123)}
        
        for x in L:
            alphaDict[x] += 1
            
        odd = 0
        for value in alphaDict.values():
            if value % 2 != 0:
                odd += 1
                
        if(odd <= 1 or len(L) == 0):
            print("yes !")
        else:
            print("no...") 
    
    
main()
