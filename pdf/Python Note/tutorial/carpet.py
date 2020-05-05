
# coding: utf-8

# In[1]:

from numpy import array,zeros,meshgrid
import matplotlib.pyplot as plt
a=array([[1,1,1],[1,0,1],[1,1,1]])
for i in range(3):
    c=3**(i+1)
    b=zeros([3*c,3*c])
    p1=array([k for k in range(c)])
    p2=array([c for k in range(len(p1))])
    for j in [0,1,2,3,5,6,7,8]:
        b[meshgrid(p1+p2*int(j/3),p1+p2*(j%3))]=a
    a=b
plt.imshow(a)
plt.show()


# In[ ]:



