class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0

        m = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                m[pattern].append(w)
        
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for n in m[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res +=1
        return 0

       