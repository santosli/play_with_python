#ZOJ Problem Set - 1002

maxNum = 0
n = 0
V = [[0 for x in range(4)] for y in range(4)]

def Canput(x, y):
	#Test if (x, y) is a safe place 
	for i in range(x-1, -1, -1):
		if (V[i][y] == 2):
			return False
		if (V[i][y] == 1):
			break
	for i in range(y-1, -1, -1):
		if (V[x][i] == 2):
			return False
		if (V[x][i] == 1):
			break
	return True

def Fire(k, curNum):
	global maxNum
	global V
	if (k == n * n):
		if (curNum > maxNum):
			maxNum = curNum
			return
	else:
		x = k / n;
		y = k % n;
		#Backtracking
		if (V[x][y] == 0 and Canput(x, y)):
			V[x][y] = 2
			Fire(k+1, curNum + 1)
			V[x][y] = 0
		Fire(k+1, curNum)
	
while (1):
	a = raw_input()
	a = a.split()
	n = int(a[0])
	if (n == 0):
		break
	#Input data
	for i in range(n):
		line = raw_input()
		for j in range(n):
			if (line[j] == '.'):
				V[i][j] = 0
			else:
				V[i][j] = 1

	#Find the maxNum
	maxNum = 0
	Fire(0,0)

	print maxNum





