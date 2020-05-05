#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# How to generate a generator:
def ex1():
	g = (x * x for x in range(10))

def ex2():
	def prod(n):
		s = 1
		for i in range(1,n+1):
			s = s*i
		return s

	def C(m,n):
		if n > m: print('wrong')
		else:
			return prod(m)//(prod(n)*prod(m-n))

	def func():
		n = 0
		while True:
			yield [C(n,j)  for j in range(n+1)]
			n += 1
	n = 0
	for i in func():
		print(i)
		n += 1
		if n >10 :break
# it's fucking difficult!
# the function will continue after each yield
# yield always return a generator which can only used in a loop
# directly produce the list is difficult, so try to split up the whole function.


def ex3():
	def is_converse(num):
		if num < 10: return True
		s = str(num)
		for i in range(0,len(s)//2):
			if s[i] != s[-i-1]: return False
		return True

	output = filter(is_converse,range(1,1000))
	print(list(output))

def ex4():
	L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
	def by_name(t):
		return str(t[0]).lower()

	def by_score(t):
		return t[1]

	L2 = sorted(L, key=by_name)
	print(L2)
	L2 = sorted(L, key=by_score)
	print(L2)


def main(argv):
	# ex2()
	# ex3()
	ex4()
if __name__ == '__main__':
	import sys
	main(sys.argv)