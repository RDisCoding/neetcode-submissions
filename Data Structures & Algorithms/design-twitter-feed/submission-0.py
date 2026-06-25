class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
         
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId)
        for i in self.followMap[userId]:
            if i in self.tweetMap:
                idx = len(self.tweetMap[i])-1
                count, tweetId = self.tweetMap[i][idx]
                minheap.append([count, tweetId, i, idx - 1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetId, i, idx = heapq.heappop(minheap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[i][idx]
                heapq.heappush(minheap, [count, tweetId, i, idx-1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
