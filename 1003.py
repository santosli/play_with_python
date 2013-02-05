#ZOJ Problem Set - 1003 Crashing Balloon
#Non-zero Exit Code....
import sys

Flag = False

def CrashIt_dfs(big, small, depth):
	global Flag
	if (big == 1 and small == 1):
		return True
	if (small == 1):
		Flag = True
	for i in range(depth, 1, -1):
		if (big % i == 0 and CrashIt_dfs(big/i, small, i-1)):
			return True
		if (small % i == 0 and CrashIt_dfs(big, small/i, i-1)):
			return True
	return False

while(1):	
	line = raw_input()
	if (len(line) == 0):
		break
	line = line.split()
	if (int(line[0]) > int(line[1])):
		a = int(line[0])
		b = int(line[1])
	else:
		a = int(line[1])
		b = int(line[0])

	if (CrashIt_dfs(a, b, 100) == False and Flag):
		print b
	else:
		print a
sys.exit(0)