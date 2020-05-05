"""the usually sorting method used in algorithm 

you can search on the wiki to find more method about sorting.
The merge way of sorting is used in Python build-in code,
which is the most efficient method for now.
The time complexity of merge sort is O(n log n),
and must use deque to achieve it, otherwise it will arise 
recrusion error.

"""
import sys
import random 
from collections import deque

def bubble(l):
    line = l
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] >= l[j]:
                l[i],l[j] = l[j],l[i]
    line,l=l,line            
    return line

def insert_s(l):
    line = l
    if len(l) is 1: return l
    for i in range(1,len(l)):
        for j in range(0,i):
            if l[i] <= l[j]: l.insert(j,l.pop(i))
    line,l=l,line            
    return line
    
#==============================================================================
# a unsuccessful way to conduct mergesort
# def merge_s(l):
#     def merge(left,right):
#         l=[]
#         for i in range(len(left)):
#             for j in range(len(right)):
#                 if left[i] < right[j]: 
#                     l.append(left[i])
#                     break
#                 else: l.append(right[j])                    
#         return l
#     middle = int(len(l) // 2)
#     left = merge_s(l[:middle])
#     right = merge_s(l[middle:])
#     return merge(left, right)
#==============================================================================

def merge_s(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_s(lst[:middle])
    right = merge_s(lst[middle:])
    return merge(left, right)


def main(argv):
    l=[random.randint(0,100) for i in range(10)]    

    print(bubble(l))
    print(insert_s(l))
    print(merge_s(l))
    print(l)

if __name__ == "__main__":
    main(sys.argv)
