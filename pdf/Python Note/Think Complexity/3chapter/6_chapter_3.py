import os
import matplotlib.pyplot as plt


def etime():
	usertime, systime, ch_usertime, ch_systime, realtime = os.times()
	return usertime + systime
	os.times()

def plot(xs,ys):
	plt.plot(xs, ys)
	scale = 'log'
	plt.xscale(scale)
	plt.yscale(scale)
	plt.title('')
	plt.xlabel('n')
	plt.ylabel('run time (s)')
	plt.show()

def main(n):
	l = []
	for i in range(n):
		l += [i]

if __name__ == '__main__':
#	n = input("type in the test number \n")
#	n = int(n)
	n = 10000000
	xs, ys = [i for i in range(n)], []
	l = []
	for i in range(n):
		start = etime()
		l += [i]
		end = etime()
		elapsed = end - start
		ys.append(elapsed)
	for i in range(1,len(ys)):
		ys[i] += ys[i-1]	
	plot(xs, ys)
