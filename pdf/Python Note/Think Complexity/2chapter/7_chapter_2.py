import string 

def alphabet_cycle():
	while True:
		for c in string.ascii_lowercase:
			yield c

def main(argv):
	abc = alphabet_cycle()
	l = 0
	for i in abc:
		print(i)
		l += 1
		if l > 30 : break


if __name__ == '__main__':
	import sys
	main(sys.argv)