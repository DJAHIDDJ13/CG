class TrieNode:
    node_count = 0
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False
        TrieNode.node_count += 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
  
    def insert(self, number):
        current = self.root
        for digit in number:
            if digit not in current.children:
                current.children[digit] = TrieNode()
            current = current.children[digit]
        current.is_end_of_number = True
  
    def search(self, number):
        current = self.root
        for digit in number:
            if digit not in current.children:
                return False
            current = current.children[digit]
        return current.is_end_of_number

N = int(input())
trie = Trie()

for i in range(N):
    trie.insert(input())

print(TrieNode.node_count - 1)