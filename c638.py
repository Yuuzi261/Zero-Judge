#Heavenly Stems List
HS = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
#Earthly Branches List
EB = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
#60 yesrs list
yearsList = [HS[i % 10] + EB[i % 12] for i in range(60)]

def main():
    while True:
        try:
            year = int(input())
        except:
            break
        
        # 1800 <= year <= 2018, 1800 is '庚申' at index 56 of yearsList
        print(yearsList[(56 + year - 1800) % 60])
    
    
main()
