import heapq
from collections import defaultdict

def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    heap = [(freq, True, char, None, None) for char, freq in frequencies.items()]  # (frequency, is_leaf, character, left, right)
    heapq.heapify(heap)

    # Build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Create a new internal node with combined frequency
        merged = (left[0] + right[0], False, None, left, right)  # (frequency, is_leaf=False, None, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root of the tree

def generate_codes(tree, prefix='', code_map=None):
    if code_map is None:
        code_map = {}

    # Leaf node: add to code map
    if tree[1]:  # Check if `is_leaf` is True
        code_map[tree[2]] = prefix
        return

    # Recursive calls for left and right children
    if tree[3]:  # Left
        generate_codes(tree[3], prefix + '0', code_map)
    if tree[4]:  # Right
        generate_codes(tree[4], prefix + '1', code_map)
    
    return code_map

def huffman_encoding(data):
    if not data:
        return "", None

    # Calculate character frequencies
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1

    # Build Huffman Tree
    tree = build_huffman_tree(frequencies)

    # Generate Huffman Codes
    codes = generate_codes(tree)

    # Encode the data
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, tree

def huffman_decoding(encoded_data, tree):
    decoded_data = []
    current_node = tree

    for bit in encoded_data:
        if bit == '0':  # Move to the left child
            current_node = current_node[3]
        else:  # Move to the right child
            current_node = current_node[4]

        if current_node[1]:  # Leaf node (is_leaf is True)
            decoded_data.append(current_node[2])  # Append the character
            current_node = tree  # Reset to root
    
    return ''.join(decoded_data)

# Example Usage
data = "Areeba Shahid"
encoded, tree = huffman_encoding(data)
print("Encoded Data:", encoded)

decoded = huffman_decoding(encoded, tree)
print("Decoded Data:", decoded)
