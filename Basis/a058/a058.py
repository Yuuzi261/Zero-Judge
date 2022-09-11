def main():
	while True:
		try:
			n = int(input())
		except:
			break
	
		x = 0
		y = 0
		z = 0
		for i in range(n):
			a = int(input())
			if a%3 == 0:
				x+=1
			elif a%3 == 1:
				y+=1
			else:
				z+=1
			
		print(x,y,z)
	
main()
