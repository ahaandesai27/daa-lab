import heapq

class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''         # (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq
        # for the heap
    
class HuffmanTree:
    def __init__(self):
        self.root = None

    def printNodes(self, node=None, val=''):
        if node is None:
            node = self.root
        newVal = val + str(node.huff)
        if node.left:
            self.printNodes(node.left, newVal)
        if node.right:
            self.printNodes(node.right, newVal)
        if not node.left and not node.right:
            print(f"{node.symbol} -> {newVal}")

    def huffman_encode(self, chars, freq):
        # Sorting the characters based on their frequency
        nodes = []
        for x in range(len(chars)): 
            heapq.heappush(nodes, Node(freq[x], chars[x])) 

        # Building the huffman tree 
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            left.huff = 0
            right.huff = 1

            newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

            heapq.heappush(nodes, newNode)

        self.root = nodes[0]

    def huffman_decode(self, string):
        res = ''
        node = self.root

        for bit in string:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            
            if node.left is None and node.right is None:
                res += node.symbol
                node = self.root
        
        return res

chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [5, 9, 12, 13, 16, 45] 
nodes = [] 
huffman = HuffmanTree()
huffman.huffman_encode(chars, freq)
huffman.printNodes()
string = "11001111001011011010"
print(huffman.huffman_decode(string))