def main():
    L = ['猴', '雞', '狗', '豬', '鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊']
    while True:
        try:
            n = int(input())
        except:
            break
            
        if n > 0:
            print(L[(n + 1911)%12])
        else:
            print(L[(n + 1912)%12])

main()
