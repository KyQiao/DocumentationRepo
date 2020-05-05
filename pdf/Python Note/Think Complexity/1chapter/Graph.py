# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 19:57:02 2017

@author: Kyqiao
"""

""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""
    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)
    
       
    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
 
    #add two dict
    def add(self,dict):
        for key in dict:
            if self.has_key(key):
                self[key].update(dict[key])
            else:
                self.update({key:dict[key]})              
        
#give two vertices and return the edge between them,if no, return 'None'
    def get_edge(self,v,w):
        try:
            return self[v][w]
        except KeyError:
            return 'None'
        except ValueError:
            return 'None'
# if use print 'None' here, the try structure would return to the remaining 
#part of the try structure, and it would print again. So one return is enough
            
#remove the given edge's vertices. Also delete the vertices
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
#==============================================================================
#         l=[]
#         for key1 in self:
#             for key2 in self[key1]:
#                 if self[key1][key2] == e:
#                     reduce(lambda [x],[y]: [x].append([y]),[l,key1,key2])
#         for i in l:
#             del self[i]
#     有些问题，直接删除self[key1],self[key2]会造成循环列表出现问题
#==============================================================================

#list all the vertice in the graph             
#    def vertices(self):
#        l=[]
#        for key in self:
#            l.append(key)
#        return l
    def vertices(self):
        return [key for key in self]

#take a vertice and return the adjacent vertices
#    def out_vertices(self,v):
#        l=[]
#        if self.has_key(v):
#            for key in self[v]:
#                l.append(key)
#        return l
    def out_vertices(self,v):
        return [key for key in self[v]]
#return the adjacent edges of a given vertice
#==============================================================================
#     def out_edges(self,v):
#         l=[]
#         if self.has_key(v):
#             for key in self[v]:
#                 l.append(self[v][key])
#         return l
#==============================================================================
    def out_edges(self,v):
        return [self[v][key] for key in self[v]]
#for a given grapg's vertices, draw the complete graph.
    def add_all_edges(self):
        l=self.vertices()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                    self.add(Graph([l[i],l[j]],[Edge(l[i],l[j])]))
#clear current edges in graph and randomly create a regular graph
    def add_regular_edges(self,degree):
        l=self.vertices()
#        can't return self 
        if degree>len(l)-1:
            raise ValueError, 'Degree must be less or equal to %s.' % str(len(l)-1)
        for i in range(len(l)):
            for j in range(i+1,len(l))+range(degree) :
                if len(self.out_vertices(l[i]))-degree:
                    self.add(Graph([l[i],l[j]],[Edge(l[i],l[j])]))            
                else:
                    continue
#the voilent way to search the connected nodes.
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
            print 'True'
        else:
            print 'False'
            
                 
            
            
        
def main(script, *args):
    c = Vertex('c')
    d = Vertex('d')
    a = Vertex('a')
    b = Vertex('b')
    ab=Edge(a,b)
    cd=Edge(c,d)
    g=Graph([a,b,c,d],[ab,cd])
#    g.add_all_edges()
#    g.add_regular_edges(2)
#    g.remove_edge(ab)
    g.is_connected()
if __name__ == '__main__':
    import sys
    main(*sys.argv)