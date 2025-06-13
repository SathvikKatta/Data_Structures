#  File: Josephus.py
#  Student Name: Saisathvik Katta
#  Student UT EID: sk49699

import sys

# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        pass
        '''##### ADD CODE HERE #####'''
        new_node = Link(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = self.first # Maintains circular flow by pointing the last item in the list back to the first item.

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):

        current_node = self.first

        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
            if current_node == self.first: # Ends the loop when every item in the list has been searched.
                break
        return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):

        find_node = self.find(data) # Checks to see if find_node is in the data.
        if find_node is None:
            return None

        current_node = self.first
        if self.first == self.last: # Runs if only one item is in the list.
            self.first = None
            self.last = None
            return find_node.data

        while current_node.next != find_node:
            current_node = current_node.next
        current_node.next = find_node.next # Make sure nothing points to find_node since that's what's being deleted.

    # Make sures the list stays circular by updating links if the first or last node of the list is deleted.
        if find_node is self.first:
            self.first = find_node.next
            self.last.next = self.first
        if find_node is self.last:
            self.last = current_node
            self.last.next = self.first

        return find_node.data

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):

        current_node = start
        for i in range(step - 1):
            current_node = current_node.next
        deleted_node = self.delete(current_node.data) # Calls the delete function to delete the selected node.
        return deleted_node, current_node.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):

        result = '['
        current = self.first
        while current is not None:
            result += str(current.data) + ', '
            current = current.next
            if current == self.first: # Stops after the whole list has been cycled through
                break
        result = result.rstrip(', ') + ']'
        return result

    # Input: Number of soldiers
    # Output: Circular list with one link for each soldier
    # Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):

    circular_list = CircularList()
    for i in range(1, num_soldiers + 1):
        circular_list.insert(i) # Creates a circular list of the numbered soldiers.
    return circular_list

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):

    current = my_list.find(start_data)
    for i in range(num_soldiers - 1):
        killed, current = my_list.delete_after(current, step_count) # Calls the delete after function to systematically kill the numbered soldiers.
        print(killed)
    print(current.data)

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''
def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)

if __name__ == "__main__":
    main()
