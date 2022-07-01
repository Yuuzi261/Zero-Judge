def main():
    while True:
        try:
            print(*[i for i in range(1, int(input())) if i % 7 != 0])
        except:
            break
    
    
main()
