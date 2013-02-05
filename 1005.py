#ZOJ Problem Set - 1005 Jugs
#The way to think

def Pour(ca, cb, n):
	curra = currb = 0
	while (currb != n):
		print "fill A"
		curra = ca
		if (curra + currb <= cb):
			print "pour A B"
			currb += curra
		else:
			print "pour A B"
			print "empty B"
			print "pour A B"
			currb = (curra + currb) % cb
	print "success"

if __name__ == "__main__":
	line = raw_input()
	line = line.split()
	Pour(int(line[0]), int(line[1]), int(line[2]))