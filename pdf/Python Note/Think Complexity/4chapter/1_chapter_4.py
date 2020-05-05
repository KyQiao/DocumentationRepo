# a implemention of fifo list

# since I have deque, I don't have a reason to use other data structures.
from collections import deque
a = deque()
a.append(4)
a.appendleft(3)
print(a.count(1))
a.extend([1,2,4])
# note that the extendleft method iter the iterable item and appendleft on the deque
# so the order of the list append on the deque is 1,2,3
a.extendleft([3,2,1])
print(a.index(4))
a.insert(0,0)
for i in range(len(a)):
	print(a.popleft())


