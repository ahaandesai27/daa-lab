import heapq
from collections import Counter
from PyPDF2 import PdfReader
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self, data):
        self.data = data
        self.frequency = Counter(self.data)
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def create_priority_queue(self):
        for char, freq in self.frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)

    def build_huffman_tree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

        return heapq.heappop(self.heap)

    def generate_codes(self, node, current_code=""):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self.generate_codes(node.left, current_code + "0")
        self.generate_codes(node.right, current_code + "1")

    def compress(self):
        self.create_priority_queue()
        root = self.build_huffman_tree()
        self.generate_codes(root)

        encoded_text = "".join([self.codes[char] for char in self.data])
        return encoded_text

    def decompress(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded_text += self.reverse_codes[current_code]
                current_code = ""

        return decoded_text

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
        # Normal read 
        with open(file, 'r') as file:
            data = file.read()
        
    huffman_generator = HuffmanTree(data)
    original_data_length = len(data)*8      # As each ascii character is 8 bits
    encoded_data = huffman_generator.compress()
    encoded_data_length = len(encoded_data)
    decoded_data = huffman_generator.decompress(encoded_data)

    assert data == decoded_data 
    
    print(f"Compression ratio for file {filename} is {round(original_data_length / encoded_data_length, 2)}. Document size reduced by {round((1 - encoded_data_length / original_data_length) * 100, 2)}%")


if __name__ == "__main__":
   compress_file("Huffman Data/compression_text1.txt")
   compress_file("Huffman Data/compression_text2.txt")
   compress_file("Huffman Data/compression_text3.docx")
   compress_file("Huffman Data/compression_text4.html")
   compress_file("Huffman Data/compression_text5.pdf")