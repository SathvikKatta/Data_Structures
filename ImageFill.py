#  File: ImageFill.py
#  Student Name: Saisathvik Katta
#  Student UT EID: sk49699


import os
import sys

# -----------------------PRINTING LOGIC, DON'T CHANGE ----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code


def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color


def print_block(color):
    print(colored(BLOCK_CHAR, color)*2, end='')

# -----------------------PRINTING LOGIC END ---------------------------


# Stack class; you can use this for your search algorithms
# Do not change.
class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


# Queue class; you can use this for your search algorithms
# Do not change.
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for search algorithms)
# it also contains a "previous color" attribute. This might be useful for your
# flood fill implementation.
# Do not change.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your
    # flood fill implementation)
    def visit_and_set_color(self, color):
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))


# class that contains the graph
# You will add code to this class.
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
        print("Adjacency matrix:")

        # Iterates over every node in the self.nodes list
        for node in self.nodes:
            adjacency_row = ''  # Creates a new string for every row in the matrix

            # Checks every each node again to see if there's an edge between them
            for each_node in self.nodes:
                if each_node.index in node.edges:
                    adjacency_row += '1'  # Adds 1 if an edge exists
                else:
                    adjacency_row += '0'  # Adds 0 if no edge exists
            print(adjacency_row)

        # empty line afterward
        print()

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")

        self.print_image()  # Prints the original image of the tower

        # Initializes sets and queue
        discovered_set = set()
        frontier_queue = Queue()

        # Adds the start_index value into the frontier queue and discovered set
        frontier_queue.enqueue(start_index)
        discovered_set.add(start_index)

        # Visits the start node (vertex) to set the initial values
        start_node = self.nodes[start_index]
        start_color = start_node.color
        start_node.visit_and_set_color(color)

        # Runs into frontier queue is not empty
        while not frontier_queue.is_empty():
            # Removes the first value in the queue and assigns the value to current index.
            current_index = frontier_queue.dequeue()

            # Explores the adjacent nodes that are the same color as the previous color.
            for adjacent_index in self.nodes[current_index].edges:
                adjacent_node = self.nodes[adjacent_index]
                if adjacent_index not in discovered_set:  # Ensures that no node is visited twice
                    if adjacent_node.color == start_color:
                        # Add adjacent node to the frontier queue and the discovered set
                        frontier_queue.enqueue(adjacent_index)
                        discovered_set.add(adjacent_index)
                        adjacent_node.visit_and_set_color(color)  # Changes the color of the adjacent node.

                        self.print_image()  # Prints the image after each color change happens

    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with

    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        # Initializes the Stack and the visited set
        vertex_stack = Stack()
        visited_set = set()

        # Creates the start node and sets the start color
        start_node = self.nodes[start_index]
        start_color = start_node.color

        # Adds the start index into the stack
        vertex_stack.push(start_index)

        # Runs the loop until the stack is empty
        while vertex_stack.size() > 0:
            # Removes the first item in the stack and assigns the value to current vertex.
            current_vertex = vertex_stack.pop()
            # Checks to make sure that there are no duplicates in the visited set.
            if current_vertex not in visited_set:
                visited_set.add(current_vertex)  # Adds current vertex to visited set.

                # Sets the current node to the current vertex and visits the current node.
                current_node = self.nodes[current_vertex]
                current_node.visit_and_set_color(color)

                # Finds the adjacent nodes of the current node and adds them to the vertex if they are the same color and not already in the visited set.
                for adjacent_index in current_node.edges:
                    adjacent_node = self.nodes[adjacent_index]

                    if adjacent_node.color == start_color:
                        if adjacent_index not in visited_set:
                            vertex_stack.push(adjacent_index)

                        self.print_image()  # Prints the image after all color changes happen

# Creates an Image Graph using input, the Color Node class and the ImageGraph class.
def create_graph(data):
    # creates graph from read in data
    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for i in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for i in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('tower.in')
    else:
        in_data = sys.stdin

    # read input
    data = in_data.read()

    # create graph
    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
