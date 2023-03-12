import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Node():
    def __init__(self, p, l, r):
        self.l_child = l
        self.r_child = r
        self.value = p
        self.parent = None
    def add_children(self, l, r):
        self.l_child = l
        self.r_child = r
    def add_parent(self, p):
        self.parent = p
    def __repr__(self):
        res = ''
        if self.parent:
            res+=f'({self.parent.value})'
        else:
            res+=f'(-)'
        if self.l_child:
            res += f'[{self.value}]({self.l_child.value},{self.r_child.value})'
        else:
            res += f'[{self.value}](-,-)'
        return res
def add_if_not(o, l=None, r=None):
    if o not in nodes:
        nodes[o] = Node(int(o), l, r)
    else:
        nodes[o].add_children(l, r)

nodes = {}
n = int(input())
v = int(input())
m = int(input())
for i in range(m):
    p, l, r = [j for j in input().split()]
    add_if_not(l)
    add_if_not(r)
    add_if_not(p, nodes[l], nodes[r])
    nodes[l].add_parent(nodes[p])
    nodes[r].add_parent(nodes[p])
root = ''
for node in nodes:
    if nodes[node].parent == None:
        root = node
        break
v_node = None
for node in nodes:
    if nodes[node].value == v:
        v_node = nodes[node]
        break
res = []
if v_node.parent == None:
    res += ['Root']
else:
    while v_node.parent != None:
        if v_node.parent.l_child == v_node:
            res += ['Left']
        else:
            res += ['Right']
        v_node = v_node.parent
print(' '.join(reversed(res)))