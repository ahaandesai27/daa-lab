import heapq
from collections import Counter
from PyPDF2 import PdfReader
from graphviz import Digraph

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq: int = freq
        self.symbol: str = symbol
        self.left: Node = left
        self.right: Node = right
        self.huff: str = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

class HuffmanTree:
    def __init__(self, data):
        self.root = None
        self.data = data
        self.mapping = {}

        self.frequencies = Counter(data)
        self.huffman_encode(list(self.frequencies.keys()), list(self.frequencies.values()))
        self.get_codes()

    def huffman_encode(self, chars, freq):
        nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]
        heapq.heapify(nodes)
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            left.huff = 0
            right.huff = 1

            newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            heapq.heappush(nodes, newNode)

        self.root = nodes[0]

    def get_codes(self, node=None, val=''):
        if node is None:
            node = self.root
        newVal = val + str(node.huff)
        if node.left:
            self.get_codes(node.left, newVal)
        if node.right:
            self.get_codes(node.right, newVal)
        if not node.left and not node.right:
            self.mapping[node.symbol] = newVal

    def compress(self):
        res = ''
        for char in self.data:
            res += self.mapping[char]
        return res

    def decompress(self, string):
        res = ''
        node = self.root
        for bit in string:
            if bit == '0':
                node = node.left
            else:
                node = node.right

            if not node.left and not node.right:
                res += node.symbol
                node = self.root

        return res
    
    def plot_huffman_tree(self, node = None, graph=None, node_id=0):
        """Generate a visual representation of the Huffman Tree using graphviz."""
        if graph is None:
            graph = Digraph(format='png')
        if node is None:
            node = self.root
        if node is not None:
            node_label = f"Freq: {node.freq}"
            if node.symbol is not None:
                node_label = f"'{node.symbol}'\nFreq: {node.freq}"
            graph.node(str(node_id), label=node_label)
            if node.left:
                graph.edge(str(node_id), str(node_id * 2 + 1), label="0")
                self.plot_huffman_tree(node.left, graph, node_id * 2 + 1)
            if node.right:
                graph.edge(str(node_id), str(node_id * 2 + 2), label="1")
                self.plot_huffman_tree(node.right, graph, node_id * 2 + 2)
        return graph

def compress_file(file):
    filename = file
    extension = file.split('.')[-1]
    if extension == 'pdf':
        with open(file, 'rb') as file:
            reader = PdfReader(file)
            data = ''
            for page in reader.pages:
                data += page.extract_text()
    else:
        with open(file, 'r') as file:
            data = file.read()

    huffman_generator = HuffmanTree(data)
    original_data_length = len(data) * 8
    encoded_data = huffman_generator.compress()
    encoded_data_length = len(encoded_data)
    decoded_data = huffman_generator.decompress(encoded_data)

    assert data == decoded_data

    print(f"Compression ratio for file {filename} is {round(original_data_length / encoded_data_length, 2)}. "
          f"Document size reduced by {round((1 - encoded_data_length / original_data_length) * 100, 2)}%")
        
    graph = huffman_generator.plot_huffman_tree()
    graph.render("Tree Output/huffmantree005")

if __name__ == "__main__":
    # compress_file("Huffman Data/compression_text1.txt")
    compress_file("Huffman Data/compression_text2.txt")
    # compress_file("Huffman Data/compression_text3.docx")
    # compress_file("Huffman Data/compression_text4.html")
    # compress_file("Huffman Data/compression_text5.pdf")
