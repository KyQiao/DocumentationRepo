# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:30:14 2017

@author: Kyqiao
"""
import random
import numpy as np
import matplotlib.pyplot as plt

class Vertex(object):
    def __init__(self, label=''):
        self.label = label
    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
    __str__ = __repr__
    
class Edge(tuple):
    def __new__(cls, *vs):
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)     
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
    __str__ = __repr__

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)          
        for e in es:
            self.add_edge(e)
    def add_vertex(self, v):
        self[v] = {}
    def add_edge(self, e):
        v, w = e
        self[v][w] = e
        self[w][v] = e
    def add(self,dict):
        for key in dict:
            if self.has_key(key):
                self[key].update(dict[key])
            else:
                self.update({key:dict[key]})              
    def get_edge(self,v,w):
        try:
            return self[v][w]
        except KeyError:
            return 'None'
        except ValueError:
            return 'None'
    def remove_edge(self,e):
        for key1 in self:
            for key2 in self[key1]:
                if self[key1][key2] == e:
                    del self[key2][key1]
                    del self[key1][key2]
                    break
    def remove_iso_vertice(self):
        for key in self:
            if self[key]=={}:
                del self[key]
    def remove_all_edges(self):
        for key in self:
            self[key]={}
    def vertices(self):
        return [key for key in self]
    def out_vertices(self,v):
        return [key for key in self[v]]
    def out_edges(self,v):
        return [self[v][key] for key in self[v]]
    def add_all_edges(self):
        l=self.vertices()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                    self.add(Graph([l[i],l[j]],[Edge(l[i],l[j])]))
    def add_regular_edges(self,degree):
        l=self.vertices()
        if degree>len(l)-1:
            raise ValueError, 'Degree must be less or equal to %s.' % str(len(l)-1)
        for i in range(len(l)):
            for j in range(i+1,len(l))+range(degree) :
                if len(self.out_vertices(l[i]))-degree:
                    self.add(Graph([l[i],l[j]],[Edge(l[i],l[j])]))            
                else:
                    continue
    def is_connected(self):
        wl=self.vertices()
        l,Q=[wl[0]],[wl[0]]

        while Q:
            current = Q.pop(0)
            for key in self[current]:
                if key not in l:
                    l.append(key)
                    Q.append(key)
        if len(l)==len(wl):
#            print 'True'
            return 1
        else:
#            print 'False'
            return 0
class RandomGraph(Graph):
    def add_random_edges(self,p):
        if p<0 and p>1:
            raise ValueError, 'p must be less or equal to 1 and greater or equal to 0'
        l=self.vertices()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if p>random.random():
                    self.add(Graph([l[i],l[j]],[Edge(l[i],l[j])])) 
                    
def main(script, *args):
    #    N=100
    #    p=arange(0.01,1,0.01)
    #==============================================================================
    # Phase = np.zeros([N-1,len(po)])
    # for (axis,n) in enumerate(labels,0):
    #     vs = [Vertex(c) for c in range(n)]
    #     g = RandomGraph(vs)
    #     for (tt,p) in enumerate(po,0):  
    #         l=0
    #         for  t in range(NN):   
    #             g.remove_all_edges()
    #             g.add_random_edges(p)
    #             l+= g.is_connected()
    #         Phase[axis,tt]=float(l)/NN         
    #==============================================================================
    
    
    
#==============================================================================
#     NN=100
#     N=40
#     po=np.arange(0.01,1,0.01)
#     labels = range(40,N+1)    
#     x,y=np.meshgrid(labels,po)
#     size=np.size(x)
#     x=x.reshape([size])
#     y=y.reshape([size])
#     Phase=np.zeros(size)
#     for i in range(size):
#         n,p=x[i],y[i]
#         vs = [Vertex(c) for c in range(n)]
#         g = RandomGraph(vs)
#         l=0
#         for  t in range(NN):   
#             g.remove_all_edges()
#             g.add_random_edges(p)
#             l+= g.is_connected()
#         Phase[i]=(float(l)/NN)
#     
#     #plt.imshow(Phase, cmap=plt.cm.gray)
#     def func(x):
#         if 0.3<x<0.8:
#             return x
#         else:
#             return 1
#     Phase=map(func,Phase)
#     plt.figure
#     plt.scatter(x,y,s=4000./N,c=Phase,lw=0.1,cmap=plt.cm.gray, vmin=0,vmax=1.0,clip_on=False)
#     plt.colorbar()
#     #plt.show()
#     plt.savefig('PhaseDirgram.png')
#==============================================================================
    
    NN=300
    N=40
    po=np.arange(0.01,1,0.01)
    labels = range(40,N+1)    
    x,y=np.meshgrid(labels,po)
    size=np.size(x)
    x=x.reshape([size])
    y=y.reshape([size])
    Phase=np.zeros(size)
    for i in range(size):
        n,p=x[i],y[i]
        vs = [Vertex(c) for c in range(n)]
        g = RandomGraph(vs)
        l=0
        for  t in range(NN):   
            g.remove_all_edges()
            g.add_random_edges(p)
            l+= g.is_connected()
        Phase[i]=(float(l)/NN)
    
    #plt.imshow(Phase, cmap=plt.cm.gray)
    def func(x):
        if 0.3<x<0.8:
            return x
        else:
            return 1
#    Phase=map(func,Phase)
    plt.figure
#    plt.scatter(x,y,s=4000./N,c=Phase,lw=0.1,cmap=plt.cm.gray, vmin=0,vmax=1.0,clip_on=False)
#    plt.colorbar()
    #plt.show()
    plt.plot(y,Phase)
    plt.savefig('PhaseDirgram.pdf')        
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
