class HuffmanNode:
    def __init__(self, symbol, count, left, right):
        self.symbol = symbol
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Allows nodes to be sorted by count
        return self.count < other.count

    def MakeEncoding(self):
        return self._MakeEncoding({}, 0, 0)

    def _MakeEncoding(self, encoding, data, nbits):
        # Recursively visit the tree to compute the bit string for each symbol.
        # The result is a dictionary such that encoding[symbol] = (data, nbits),
        # a tuple that represents the variable number of bits in the encoding.
        if self.symbol is not None:
            encoding[self.symbol] = (data, nbits)
        if self.left is not None:
            self.left._MakeEncoding(encoding, data << 1, 1+nbits)
        if self.right is not None:
            self.right._MakeEncoding(encoding, 1 | (data << 1), 1+nbits)
        return encoding

    def TreeTuple(self):
        # Convert the tree into a tuple format.
        # Each internal node becomes a tuple (left, right).
        # Each leaf node is just the symbol by itself.
        if self.symbol is not None:
            return self.symbol
        return (self.left.TreeTuple(), self.right.TreeTuple())

    def SourceCode(self):
        return repr(self.TreeTuple()).replace(' ', '')
