from structs import Graph
from structs import Trie
from board import *
from visualizer import *
import numpy as np
import cv2

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

# early stopping using trigram matching
def wordSearch3(start_index, G, dictionary, trigram_dict ,words, frames, prefix="", visited=None):
    if visited==None:
        visited = []
    
    start = G.get_node_val(start_index)
    prefix += start
    visited.append(start_index)
        
    if dictionary.search(prefix) and not prefix in words:
        words.append(prefix)
        
    for n in G.get_neighbours(start_index):
        letter = G.get_node_val(n)
        if dictionary.is_prefix(prefix + letter) and not n in visited:

            if len(prefix + letter) >= 3:
                trigram = (prefix + letter)[-3:]
                if not trigram_dict.search(trigram):
                    continue

            wordSearch3(start_index=n, 
                       G=G, 
                       dictionary=dictionary, 
                       trigram_dict=trigram_dict,
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




def solveBoard(n, G, dictionary, words):
    for i in range(n * n):
        wordSearch(i, G, dictionary, words)
        
def solveBoard2(n, G, dictionary, words, frames):
    for i in range(n * n):
        wordSearch2(i, G, dictionary, words, frames)

def solveBoard3(n, G, dictionary, trigram_dict ,words, frames):
    for i in range(n * n):
        wordSearch3(i, G, dictionary, trigram_dict, words, frames)

def createDictionary(filepath, dictionary):
    f = open(filepath, 'r')
    lines = f.readlines()
    for line in lines:
        word = line.strip()
        dictionary.insert(word)
    return dictionary

board_letters = "mdacofhraueumnne"
G = create_board(board_letters, 4)
dictionary = createDictionary('vocabulary/scrabble_wordbank_2019.txt', Trie())
trigram_dict = createDictionary('vocabulary/trigram_table.txt', Trie())

# prints board
print_board(4, G)
    
words = []
frames = []
# print(wordSearch(0, G, dictionary, words))
# print(wordSearch(1, G, dictionary, words))
# solveBoard(4, G, dictionary, words)
# solveBoard2(4, G, dictionary, words, frames)
print(words)
print()
print("sorted by length:")
print(sorted(words, key=len))
print()

# visualizer params
img_dims = 512
lett_per_row = 4
font_face = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
font_scale = 2
# frames_data = [[0, 1, 4, 9], [1, 2, 5, 9]] # JUST FOR TESTING

solveBoard3(4, G, dictionary, trigram_dict, words, frames)
rendered_frames = draw_frames(frames, img_dims, lett_per_row, thickness, font_face, font_scale, board_letters, font_face)
create_mp4(rendered_frames, img_dims)