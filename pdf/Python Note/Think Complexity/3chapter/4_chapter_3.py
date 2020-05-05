import string

class LinearMap(object):

	def __init__(self):
		self.items = []

	def add(self,k,v):
		self.items.append((k,v))
		#add a tuple to the list

	def get(self,k):
		for key ,val in self.items:
			if key == k:
				return val
		raise KeyError
		#remember the common form in the syntaxn

class BetterMap(object):

	def __init__(self,n=100):
		self.maps = []
		for i in range(n):
			self.maps.append(LinearMap())
#initiate a n LinearMap list. n=100 on default

	def find_map(self,k):
		index = hash(k) %len(self.maps)
		#self.maps return a list of LinearMap, 
		#We initiate the BMap with 100 LMap, but you can change the number of the Lmap in BMap.
		#Once the Bmap inititated, we use the hash func to give the index.
		#different object can export the same hash value, while the same value must can return the same 
		#hash value. So if the input number of paris is n, and the Lmap number is defaultly set as 100,
		#thus per Lmap has n/100 items in itself.
		#Obivously we can say the Bmap is 100 times faster than the Lmap.

		return self.maps[index]

# use the hash value as the index?
# so what is that?
#hash function return a integer in the Python. The limit of the function is that it can only return 
#the inmutable object in Python. List and dictionary are mutable types.

	def add(self,k,v):
		m = self.find_map(k)
		m.add(k,v)
#m is a LinearMap, so you can use the add method in it.

	def get(self,k):
		m = self.find_map(k)
		return m.get(k)	
#So if you looking for k key in the Map, first return the hash key in the BMap,then import the value in
#the LinearMap.
#Thus means the class use hash to accelerate the look-up process after all.

class HashMap(object):
	def __init__(self):
		self.maps = BetterMap(2)
		self.num = 0

	def get(self,k):
		return self.maps.get(k)

	def add(self, k, v):
		if self.num == len(self.maps.maps):
			self.resize()

		self.maps.add(k,v)
		self.num += 1 
		#make sure the average number in Lmap is 1.
		#Does this look reliable as it seems?

	def resize(self):
		new_maps = BetterMap(self.num * 2)

		for m in self.maps.maps:
			for k, v in m.items:
				new_maps.add(k, v)





def main(argv):
	m = HashMap()
	s = string.ascii_lowercase

	for k, v in enumerate(s):
		m.add(k, v)


	for k in range(len(s)):
		print(k,m.get(k))

if __name__ == '__main__':
	import sys

	main(*sys.argv)
