def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i

    return f

def main():
    while True:
        try:
            n = int(input())
        except:
            break

        print(int(factorial(2 * n)/(factorial(n + 1)*factorial(n))))

main()
