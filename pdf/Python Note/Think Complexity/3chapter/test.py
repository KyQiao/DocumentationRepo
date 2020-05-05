# coding=utf-8
 
def main(l):
	for i in range(len(l)):
		print(l[i])

if __name__ == '__main__':
	import sys
	print("the function take in abitray int numbers"%())
#you should modify the arg variable in this place.
#and clarify the form of the input 
	n=input("input a string: \n")

	l=[int(sys.argv[i]) for i in range(1,len(sys.argv))	]
	main(n)
	main(l)
	print(type(n))
#always remember that the first argv python take in is the name of the code, so the real
#parameter is the no.1 in the main function.

#and the indentation is also a problem. The "tab" and "space" are two different way in Python.


#As you can see, the python can import the parameter via the input function.
#The input function always regards the data as str, so you have to ocnvert it to other forms.