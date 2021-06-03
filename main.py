import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
alphabet_ascii = []
alphabet = "abcdefghijklmnopqrstuvwxyz?"

for i in range(h):
    row = input()
    alphabet_ascii.append(row)

#Finding the index of each letter in the alphabet
indexes=[]
for letter in t:
    for i,let in enumerate(alphabet):
        if let==letter.lower(): 
            indexes.append(i) 
            break
    else: indexes.append(-1)
    
#print(f"l={l}, h={h}, and letter={t}, index={indexes}")

#Writing in ASCII Format
for i in range(h):
    for j in indexes:
        if j!=-1: print(alphabet_ascii[i][j*l:(j*l)+l], end="")
        else: print(alphabet_ascii[i][-l:], end="")
    print("")
