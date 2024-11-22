from Graph import Graph
from Trie import Trie
from gridfunctions import *

def main():
    G = Graph()
    dictionary = Trie()

def render():
    # draws board
    pass
    
def drawBoard():
    # draws the arrows
    pass

def clearBoard():
    # clears the board of all arrows
    pass
    
def eraseArrow():
    # used in draw board
    pass


# iteratively builds solution using dfs approach (finds all words starting with start_index)

def wordSearch(start_index, G, dictionary, prefix="", visited=[], words=[]):
    start = G.get_node_val(start_index)
    prefix += start
    visited.append(start_index)
        
    if dictionary.search(prefix) and not prefix in words:
        words.append(prefix)
    
    # continue traversing neighbours for prefixes
    for n in G.get_neighbours(start_index):
        letter = G.get_node_val(n)
        if dictionary.is_prefix(prefix + letter) and not n in visited:
            wordSearch(start_index=n, G=G, dictionary=dictionary, prefix=prefix, visited=visited.copy(), words=words)
        
    return words

G = generate_grid([
    ["w", "o", "r", "d"], 
    ["b", "a", "n", "k"], 
    ["s", "a", "m", "p"], 
    ["l", "e", "a", "a"]])

dictionary = Trie()

f = open('wordbank.txt', 'r')
lines = f.readlines()
for line in lines:
    word = line.strip()
    dictionary.insert(word)
    
print(wordSearch(0, G, dictionary))