import sys

def main():
    for s in sys.stdin :
        a = []
        a = s
        for i in range(len(a)):
            print(chr(ord(a[i])-7),end = '')
        print('\n')
    
main()
