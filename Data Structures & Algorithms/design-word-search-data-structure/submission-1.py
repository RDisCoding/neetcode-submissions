class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0]*26
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("#")

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if not ptr.children[ord(c) - ord('a')]:
                ptr.children[ord(c) - ord('a')] = TrieNode(c)
            ptr = ptr.children[ord(c) - ord('a')]
        ptr.flag = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in range(len(word)):
            if word[c] == ".":
                for child in ptr.children:
                    if child: 
                        return self.subsearch(child, word[c+1:])
            else:
                if not ptr.children[ord(word[c]) - ord('a')]: 
                    return False
                ptr = ptr.children[ord(word[c]) - ord('a')]
        return ptr.flag
    
    def subsearch(self, node, word):
        ptr = node
        for c in range(len(word)):
            if word[c] == ".":
                for child in ptr.children:
                    if child:
                        return self.subsearch(child, word[c+1:])
                return False
            else:
                if not ptr.children[ord(word[c]) - ord('a')]:
                    return False
                ptr = ptr.children[ord(word[c]) - ord('a')]
        return ptr.flag
                

