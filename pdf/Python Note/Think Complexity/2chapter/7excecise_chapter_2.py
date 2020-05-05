import string 

def alphanumeric(n):
	l = -1
	s=1
	while s < n:
		for c in string.ascii_lowercase:
			l += 1
			s = l//26 + 1
			yield c+str(s)


def main(argv):
	a = alphanumeric(3)
	l = []
	for i in a :
		l.append(i)
	print(l)
#	print(dir(a))
if __name__ == '__main__':
	import sys
	main(sys.argv)
