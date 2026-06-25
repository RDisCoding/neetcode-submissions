class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0]*26
        self.flag = False        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode("#")
        res = set()

        for word in words:
            ptr = root
            for c in word:
                if not ptr.children[ord(c) - ord('a')]:
                    ptr.children[ord(c) - ord('a')] = TrieNode(c)
                ptr = ptr.children[ord(c) - ord('a')]
            ptr.flag = True
        
        def bt(i,j,ptr,word):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] == "#" or not ptr.children[ord(board[i][j])-ord('a')]:
                return 

            if ptr.children[ord(board[i][j])-ord('a')]:
                word.append(board[i][j])
                ptr = ptr.children[ord(board[i][j])-ord('a')]
                if ptr.flag == True:
                    res.add("".join(word))
                    

            temp = board[i][j]
            board[i][j] = "#"
            bt(i-1,j,ptr,word)
            bt(i+1,j,ptr,word)
            bt(i,j-1,ptr,word)
            bt(i,j+1,ptr,word)
            board[i][j] = temp
            word.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                bt(i,j,root,[])
        
        return list(res)
                
            