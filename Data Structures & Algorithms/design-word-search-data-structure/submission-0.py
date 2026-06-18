class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = [None]*26
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("#")

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                ptr.children[i] = TrieNode(c)
            ptr = ptr.children[i]
        ptr.flag = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            if not root: return False
            ptr = root

            for i in range(j, len(word)):
                c = word[i]
                idx = ord(c) - ord('a')
                if c==".":
                    for child in ptr.children:
                        if dfs(i+1, child): 
                            return True
                    return False
                else:
                    if not ptr.children[idx]:
                        return False
                    ptr = ptr.children[idx]
            return ptr.flag
        
        return dfs(0, self.root)
        

        
