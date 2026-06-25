class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0]*26
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("#")

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if not ptr.children[ord(c) - ord('a')]:
                ptr.children[ord(c) - ord('a')] = TrieNode(c)
            ptr = ptr.children[ord(c) - ord('a')]
        ptr.flag = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if not ptr.children[ord(c) - ord('a')]:
                return False
            ptr = ptr.children[ord(c) - ord('a')]
        return ptr.flag
        
    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if not ptr.children[ord(c) - ord('a')]:
                return False
            ptr = ptr.children[ord(c) - ord('a')]
        return True
        