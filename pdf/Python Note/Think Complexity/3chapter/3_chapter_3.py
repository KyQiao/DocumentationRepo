"""
The bisection search method, using the bisect module	
and the baisc part of import parameter into python vai the shell
"""

from bisect import *

def bisearch(lst,item):
	lst = sorted(lst)
	index=bisect_left(lst,item)
	if lst[index] == item: print('The item(%d) is located in the %d column of the list' % (item ,index+1))
	else: print("item(%d) is not exist" % (item))
	
def main(n,item):
	l = [2*i+1 for i in range(n)]
	bisearch(l,item)

if __name__ == '__main__':
	import sys
	n = input("create the list \n")
	item = input("the item you want to find is \n")


	main(int(n),int(item))