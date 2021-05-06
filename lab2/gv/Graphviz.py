from graphviz import Digraph

g = Digraph('Traffic light')
g.node(name='Green',color='green')
g.node(name='Yellow',color='yellow')
g.node(name='Red',color='red')
g.edge('Green','Green',"Keep Green",color='green')
g.edge('Green','Yellow',"Green2Yellow",color='yellow')
g.edge('Yellow','Yellow',"Keep Yellow",color='yellow')
g.edge('Yellow','Red',"Yellow2Red",color='red')
g.edge('Red','Red',"Keep Red",color='red')
g.edge('Red','Green',"Red2Green",color='green')
g.view()
