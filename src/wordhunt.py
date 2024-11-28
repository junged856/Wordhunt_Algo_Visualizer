from structs import Graph
from structs import Trie
from grid_utils import *

# iteratively builds solution using dfs approach (finds all words starting with start_index)

def wordSearch(start_index, G, dictionary, words, prefix="", visited=None):
    if visited==None:
        visited = []
    
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

# supports the ability to see algorithm visually by using frames 

def wordSearch2(start_index, G, dictionary, words, frames, prefix="", visited=None):
    if visited==None:
        visited = []
    
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
            # only add meaningful frames
            if not n in visited:
                visited2 = visited.copy()
                visited2.append(n)
                frames.append((visited2, prefix + letter, words.copy())) 
                
    return frames 

# just gets words
def solveBoard(n, G, dictionary, words):
    for i in range(n * n):
        wordSearch(i, G, dictionary, words)
        
# gets words + frames
def solveBoard2(n, G, dictionary, words, frames):
    for i in range(n * n):
        wordSearch2(i, G, dictionary, words, frames)

def createDictionary(filepath, dictionary):
    f = open(filepath, 'r')
    lines = f.readlines()
    for line in lines:
        word = line.strip()
        dictionary.insert(word)
    return dictionary

G = generate_grid("mdacofhraueumnne", 4)
dictionary = createDictionary('vocabulary/scrabble_wordbank_2019.txt', Trie())

# visualize the board
draw_grid(4, G)

    # this is what the grid should look like:
    # ["l", "e", "e", "a"], 
    # ["h", "y", "w", "a"], 
    # ["r", "s", "c", "r"], 
    # ["p", "k", "c", "h"]]
    
words = []
frames = []
# print(wordSearch(0, G, dictionary, words))
# print(wordSearch(1, G, dictionary, words))
# solveBoard(4, G, dictionary, words)
wordSearch2(0, G, dictionary, words, frames)
print(words)
print()
print("sorted by length:")
print(sorted(words, key=len))
print()