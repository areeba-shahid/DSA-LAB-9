Lab 9: Huffman Coding
Objective
The objective of this lab is to implement Huffman Coding, a popular algorithm used for lossless data compression. The goal is to represent the characters of a given text with variable-length codes, where the most frequent characters are represented by shorter codes, and less frequent characters are represented by longer codes.

Key Concepts
Huffman Coding Overview:
Huffman coding is a greedy algorithm that works by assigning variable-length codes to input characters based on their frequencies. The key idea is to:

Build a frequency table for the characters in the input.
Use this frequency table to build a binary tree, called the Huffman Tree, where:
The leaf nodes represent characters.
Internal nodes represent merged frequencies of their child nodes.
Traverse the tree to generate the Huffman codes, where:
Each left child edge represents 0.
Each right child edge represents 1.
Steps:
Calculate frequencies of each character in the input.
Build a priority queue (min-heap) to store the characters based on their frequencies.
Build the Huffman Tree by repeatedly extracting the two nodes with the smallest frequencies and merging them.
Generate the Huffman codes by traversing the tree.
Example:
For the string "ABRACADABRA", the frequency of characters would be:

A: 5
B: 2
R: 2
C: 1
D: 1
The resulting Huffman Tree would generate a set of codes such as:

A: 0
B: 10
R: 11
C: 1100
D: 1101
Approach
We'll implement the following steps:

Frequency Calculation: Calculate the frequency of each character in the given string.
Min-Heap for Tree Construction: Use a priority queue (min-heap) to store characters based on their frequencies.
Huffman Tree Creation: Construct the Huffman Tree by merging nodes with the lowest frequencies.
Code Generation: Traverse the tree to assign codes to characters.
Encoding: Encode the input string based on the Huffman codes.
Decoding: Decode the encoded string back to the original text using the Huffman Tree.
