from structs import Graph
from structs import Trie
from grid_utils import *

def main():
    G = Graph()
    dictionary = Trie()

def renderBoard():
    # draws board
    
    pass
    
def animateArrows():
    # draws the arrows
    pass

def animateWordsFound():
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

# adding ability to see algorithm visually by using frames 

def wordSearch2(start_index, G, dictionary, frames=[], prefix="", visited=[], words=[]):
    start = G.get_node_val(start_index)
    prefix += start
    visited.append(start_index)
        
    if dictionary.search(prefix) and not prefix in words:
        words.append(prefix)
        
    # continue traversing neighbours for prefixes until no prefix found
    for n in G.get_neighbours(start_index):
        letter = G.get_node_val(n)
        if dictionary.is_prefix(prefix + letter) and not n in visited:
            wordSearch2(start_index=n, 
                       G=G, 
                       dictionary=dictionary, 
                       frames=frames, 
                       prefix=prefix, 
                       visited=visited.copy(), 
                       words=words)
        else:
            # once a dead-end is hit, copy the path, words found, and letters traversed (single frame)
            visited2 = visited.copy()
            visited2.append(n)
            frames.append((visited2, prefix + letter, words.copy())) # each item contains all info needed to render a single frame
    return frames 

G = generate_grid("ndubiehlaaoeihsw", 4)

draw_grid(4, G)

    # this is what the grid should look like:
    # ["n", "d", "u", "b"], 
    # ["i", "e", "h", "l"], 
    # ["a", "a", "o", "e"], 
    # ["i", "h", "s", "w"]]

dictionary = Trie()

f = open('vocabulary/wordbank.txt', 'r')
lines = f.readlines()
for line in lines:
    word = line.strip()
    dictionary.insert(word)

frames = wordSearch(1, G, dictionary)
print(frames)