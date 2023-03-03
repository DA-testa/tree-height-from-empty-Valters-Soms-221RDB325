# python3
import sys
import threading
import numpy

def compute_height(n, parents):
    max_height = 0
    for x in range(n):
        height = 0
        y = x
        while y != -1:
            height = height + 1
            y = parents[y]
        max_height = max(max_height, height)
    return max_height

def main():
    input_text = input()
    if 'F' in input_text:
        input_file = input()
        input_file = "test/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    n = int(f.readline())
                    parents = numpy.array(list(map(int, f.readline().split())))
                    print(compute_height(n, parents))

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
        print(compute_height(n, parents))
    
        
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()