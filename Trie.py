class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root 
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True
        
    def search(self, word: str) -> bool:
        current = self.root 
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False 
            current = current.children[index]
        return current.isLeaf
    
    # used for prefix searching
    def is_prefix(self, prefix: str) -> bool:
        current = self.root 
        for letter in prefix:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return True