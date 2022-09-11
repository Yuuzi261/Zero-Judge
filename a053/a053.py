def main():
	while True:
		try:
			n = int(input())
		except:
			break
		
		s = 0	
		if 0 <= n <= 10:
			for i in range(n):
				s+=6
		elif 11<= n <= 20:
			s = 60
			for i in range(n-10):
				s+=2
		elif 21 <= n <= 40:
			s = 80
			for i in range(n-20):
				s+=1
		else:
			s = 100
			
		print(s)
	
main()
