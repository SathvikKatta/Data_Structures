#  File: BST_Cipher.py
#  Student Name: Saisathvik Katta
#  Student UT EID: sk49699

import sys

# One node in the BST Cipher Tree
class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None

# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):

        self.root = None
        self.key = key

        # Sends the key through the clean function, to remove invalid characters that shouldn't be printed in the key.
        self.key = self.clean(key)

        # For every valid character in the key uses the insert function to add them to the tree.
        for character in self.key:
            self.insert(character)

    # Inserts one new character/Node to the BST Cipher tree if it doesn't already exist in the tree.
    def insert(self, ch):

        new_node = Node(ch)

        # Sets root to new node if the tree is empty.
        if self.root is None:
            self.root = new_node
        else:
            currentNode = self.root
            while currentNode is not None:
                # Runs if the character in the key is less than the data of the current node.
                if ch < currentNode.ch:
                    if currentNode.left is None:
                        currentNode.left = new_node
                        break
                    else:
                        currentNode = currentNode.left
                # Runs if the character in the key is greater than the data of the current node.
                elif ch > currentNode.ch:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        break
                    else:
                        currentNode = currentNode.right
                else:  # If the character already exists in the tree, nothing more is added to the tree.
                    break

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):

        encrypted_message = ''
        for ch in message:
            if self.isValidCh(ch):  # Checks if the character is valid using the isValidCh function.
                encrypted_message += self.encrypt_ch(ch)  # Encrypts the character using the BST Tree.
        return encrypted_message[:-1]

    # Encrypts a single character at a time
    def encrypt_ch(self, ch):

        encrypted_character = ''
        current = self.root
        if current.ch == ch:
            encrypted_character += '*' # Returns "*" if that's the root of the tree

        while current is not None:
            if ch == current.ch: # Exits the Loop when the character is found in the tree
                break
            # Adds "<" to the encrypted_character string if we move left in the BST Tree when finding the character.
            elif ch < current.ch:
                encrypted_character += '<'
                current = current.left
            # Adds ">" to the encrypted_character string if we move right in the BST Tree when finding the character.
            else:
                encrypted_character += '>'
                current = current.right
        # Adds "!" to the encrypted_character string to indicate that the encrypted code for the letter is complete.
        if current is not None:
            return encrypted_character + '!'
        # Returns nothing if the character is not found in the tree.
        else:
            return ''


    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):

        decrypted_message = ''
        current = self.root
        decrypt_character = ''
        for character in codes_string:
            if character == '!':
                decrypted_message += self.decrypt_code(decrypt_character) # Decrypts the code for the character once the "!" symbol is reached.
                decrypt_character = '' # Resets the code for each character.
                current = self.root # Sets current back to the root.

            # Changes the current node to the left if "<" is read in the codes_string string.
            elif character == '<':
                if current.left == None:
                    decrypt_character += '<'
                    continue # Continues to next node in tree if the value of the node is none, avoids a None type error
                else:
                    current = current.left
                    decrypt_character += '<'
            # Changes the current node to the right if ">" is read in the codes_string string.
            elif character == '>':
                if current.right == None:
                    decrypt_character += '>'
                    continue # Continues to next node in tree if the value of the node is none, avoids a None type error
                else:
                    current = current.right
                    decrypt_character += '>'

        # Appends the character if the last letter is valid
        if self.isValidLetter(current.ch):
            decrypted_message += current.ch
        return decrypted_message

    # Decrypts a single letter.
    def decrypt_code(self, code):
        node = self.root
        for i in code:
            if i == '<':
                if node.left == None: # Returns an empty string if the search on the left for the letter leaves the tree.
                    return ''
                node = node.left
            elif i == '>':
                if node.right == None: # Returns an empty string if the search on the right for the letter leaves the tree.
                    return ''
                node = node.right

        # Checks if the node is valid using the isValidCh function before returning the code.
        if node and self.isValidCh(node.ch):
            return node.ch
        else:
            return ''

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''
def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
