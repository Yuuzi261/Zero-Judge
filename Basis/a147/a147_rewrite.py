#slower than a147.py
def main():
    while True:
        try:
            [print(i, end = ' ') for i in range(1, int(input())) if i % 7 != 0], print()
        except:
            break
        
        
main()
