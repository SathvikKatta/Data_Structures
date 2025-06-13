#  File: HuffmanCodes.py
#  Student Name: Saisathvik Katta
#  Student UT EID: sk49699
# Python Huffman Compression
from PriorityQueue import PriorityQueue
import sys


# Huffman Node Class

class Huffman_Node(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        if self.ch is None:
            ch = "*"
        else:
            ch = self.ch
        return ch + ", " + str(self.count)


# Build Character Frequency Table
# uses dictionary
# characters added in the order they first occur
def build_char_freq_table(inputString):

    # ADD CODE HERE
    # The code takes an input string and creates a frequency table of characters.

    # Initializes the table as an empty dictionary.
    table = {}

    # This loop checks if the character is already in the table dictionary.
    for char in inputString:
        if char != '\n':
            if char == '<':
                char = "<space>"

            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
    return table


# Builds the Huffman Tree
# Creates Huffman Nodes, some pointing to others.
# Returns the root node
def build_huffman_tree(inputString):
    # Build the frequency table, a dictionary of character, frequency pairs
    freq_table = build_char_freq_table(inputString)

    # Build a priority queue, a queue of frequency, character pairs
    # Highest priority is lowest frequency
    # When a tie in frequency, first item added will be removed first
    priorities = PriorityQueue()
    for key in freq_table:
        node = Huffman_Node(ch=key, count=freq_table[key])
        priorities.push(node)

    # Builds internal nodes of huffman tree, connects all nodes

    # The loop continues until there's only one node left in the 'priorities' queue.
    # Creates the tree from the bottom up.
    # This loop creates the huffman tree.
    while (priorities.get_size() > 1):
        # ADD CODE HERE
        left_tree = priorities.pop()
        right_tree = priorities.pop()
        count_tree = left_tree.count + right_tree.count
        new_node = Huffman_Node(count=count_tree, left=left_tree, right=right_tree)

        # Pushes the new node back into the priority queue
        priorities.push(new_node)

    # At the end, priority queue is empty
    # Return the root node of the Huffman Tree
    return priorities.pop()

# After Huffman Tree is built, create dictionary of
# characters and code pairs
def get_huffman_codes(node, prefix, codes):
    if (node.left is None and node.right is None):
        codes[node.ch] = prefix
    else:
        get_huffman_codes(node.left, prefix + "0", codes)
        get_huffman_codes(node.right, prefix + "1", codes)
    return codes

# For each character in input file, returns the Huffman Code
# Input file uses <space> to indicate a space
# If character not found, display "No code found"
def process_chars(data, huff_codes):

    # ADD CODE HERE

    print("Character    Code")

    # This loop processes characters from the provided data, then checks their Huffman codes in the dictionary.
    # Then the loop prints out the corresponding code, or a message that says no code if no character was found.

    for line in data[1:]:
        characters = line.strip()[0]
        if characters == "<":
            characters = " "
        else:
            characters = characters

        # Checks to see if characters is in huff_codes.
        if characters in huff_codes:
            print(f'{characters:<11}  {huff_codes[characters]}')
        else:
            print(f'{characters:<11}  No code found')


''' DRIVER CODE '''

# Open input source
# Change debug to false before submitting
debug = True
if debug:
    in_data = open('message.in')
else:
    in_data = sys.stdin

# read message
data = in_data.readlines()
message = data[0].strip()

# Build Huffman Tree and Codes
root = build_huffman_tree(message)
huff_codes = get_huffman_codes(root, "", {})

# display code for each character in input file
process_chars(data, huff_codes)



