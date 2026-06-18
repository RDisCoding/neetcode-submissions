class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0]*26
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("#")
        self.root.ptr = self.root

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            print(i)
            if not ptr.children[i]:
                ptr.children[i] = TrieNode(c)
            ptr = ptr.children[i]
        
        ptr.flag = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                return False
            ptr = ptr.children[i]
        
        return ptr.flag

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                return False
            ptr = ptr.children[i]
        
        return True
        