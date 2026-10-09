CS121 Assignment 1 - Word Frequencies and File Intersection

What It Does

PartA.py counts how often each word appears in one text file.
PartB.py counts how many different words two text files share.

How to Run

Keep PartA.py and PartB.py in the same folder (PartB imports PartA).

Part A
python3 PartA.py myfile.txt

Part B
python3 PartB.py file1.txt file2.txt

Part A prints word - count lines, most frequent first, ties alphabetical.
Part B prints one number: how many different words appear in both files.

What Counts as a Word

A run of letters and digits, lowercased. Everything else (spaces, punctuation, non-English characters) separates words.

Part A Functions

tokenize(path)
Reads the file line by line and builds a list of words, character by character.
O(n)

computeWordFrequencies
Counts each word in a dictionary.
O(m)

printFrequencies
Prints words by count using a heap. Counts are stored negative because Python's heap is a min-heap, which also gives alphabetical order on ties.
O(k log k)

Part B Function

count_common_tokens
Tokenizes both files (reusing Part A), turns each list into a set, and returns the size of the intersection. A set drops repeats, so each shared word counts once.
O(n1 + n2)
