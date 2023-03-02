# python3
import sys
import threading
import numpy

class node_ob:
    def __init__(self, parent, child=None):
        self.parent = parent
        self.child = child
    def addCh(self, node):
        if self.child is None: 
            self.child = []
        self.child.append(node) 

def compute_height(node):

    if node.child is None:
        return 0
    children = node.child
    deep_list = []
    for child in children:
        deep_list.append(compute_height(child))
    return max(deep_list, default=0) + 1


def main():

    input_text = input()
    if input_text == 'F':

        input_file = input()
        if "a" not in input_file:

            try:
                with open(input_file,mode = 'r') as f:
                    n = f.readline()
                    parents = f.readline()
                f.close()

                node_list = []
                for i in range(n):
                    node_list.append(node_ob(parents[i]))

                for ch_index in range(n):
                    par_index = parents[ch_index]
                    if par_index == -1:
                        root = ch_index
                    else:
                        node_list[par_index].addCh(node_list[ch_index])
                
                if len(node_list) == 0:
                    return 0

                height = compute_height(node_list[root]) + 1
                print(height)
                return 0

            except FileNotFoundError:
                print("File not found")
                return 0

    if input_text == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
        node_list = []
        for i in range(n):
            node_list.append(node_ob(parents[i]))

        for ch_index in range(n):
            par_index = parents[ch_index]
            if par_index == -1:
                root = ch_index
            else:
                node_list[par_index].addCh(node_list[ch_index])
                if len(node_list) == 0:
                    return 0
        height = compute_height(node_list[root]) + 1
        print(height)
        return 0

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()