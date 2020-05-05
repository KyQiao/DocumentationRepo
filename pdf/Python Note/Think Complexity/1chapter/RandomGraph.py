# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:30:14 2017

@author: Kyqiao
"""
import string
import random
import math

from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas

from Graph import Vertex
from Graph import Edge
from Graph import Graph
from GraphWorld import GraphCanvas
from GraphWorld import GraphWorld
from GraphWorld import Layout
from GraphWorld import CircleLayout
from GraphWorld import RandomLayout

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
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:10]]

    # create a graph and a layout
    g = Graph(vs)
    g.add_all_edges()
#    g.remove_edge(Edge(vs[1],vs[2]))
#    g.add_regular_edges(9)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
    g.is_connected()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
