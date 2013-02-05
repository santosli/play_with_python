# s = raw_input()
# a = s.split()

# print "The sum is :",int(a[0]) + int(a[1])

import sys
for line in sys.stdin:
    a = line.split()
    print int(a[0]) + int(a[1])