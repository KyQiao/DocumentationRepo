# -*- coding: utf-8 -*-
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
            
#remove the given edge's vertices.
    def remove_edge(self,e):
        l=[]
        for key1 in self:
            for key2 in self[key1]:
                if self[key1][key2] == e:
                    del self[key2][key1]
                    del self[key1][key2]
                    break
        for key1 in self:
            if self[key1]=={}:
                l.append(key1)
        for i in l:
            del self[i]
            
    def vertices(self):
        return [key for key in self]

#take a vertice and return the adjacent vertices
    def out_vertices(self,v):
        return [key for key in self[v]]
#return the adjacent edges of a given vertice
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

def main(script, *args):
    c = Vertex('c')
    d = Vertex('d')
    a = Vertex('a')
    b = Vertex('b')
    g=Graph([a,b,c,d],[])
    g.add_all_edges()
#    g.add_regular_edges(2)
    print g
    print g.out_vertices(a)
    print g.out_edges(a)
if __name__ == '__main__':
    import sys
    main(*sys.argv)