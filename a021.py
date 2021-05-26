import sys
def main():
    for s in sys.stdin:
        a = s
        a = eval(a.replace('/','//'))
        print(a)
        
main()
