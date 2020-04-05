import math
def main():
	while True:
		try:
			n = int(input())
		except:
			break
		
		L = []
		for i in range(n):
			sum = 0
			a = int(input())
			b = int(input())
			c = int(math.sqrt(a))
			d = int(math.sqrt(b))
			for k in range(c,d+1):
				if(a <=k**2<= b):
					sum+=k**2
			L.append(sum)
		
		for i in range(len(L)):
			print("Case ",i+1,": ",L[i],sep = '')
	
main()
