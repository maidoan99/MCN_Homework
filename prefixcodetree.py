class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def isLeave(self):
        return (self.right is None) and (self.left is None)


class PrefixCodeTree:
    def __init__(self):
        self.root = Node('')

    def insert(self, codeword, symbol):
        node = self.root

        for code in codeword:
            if (code == 0):
                if (node.left is None):
                    node.left = Node('')
                    node = node.left
                else:
                    node = node.left
            else:
                if (node.right is None):
                    node.right = Node('')
                    node = node.right
                else:
                    node = node.right

        node.data = symbol


    def decode(self, encodedData, datalen):
        data = ''
        result = ''
        node = self.root

        # Convert encodedData to bit data
        for byte in encodedData:
            data += f'{byte:08b}'

        # Decode encodedData
        for i in range(datalen):
            if (data[i] == '0'):
                node = node.left
            else:
                node = node.right

            if (node.isLeave()):
                result += node.data
                node = self.root
        return result


if __name__ == '__main__':
    codeTree = PrefixCodeTree()

    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }

    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    print(codeTree.decode(b'\xd2\x9f\x20', 21))