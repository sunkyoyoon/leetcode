class Twitter:

    def __init__(self):
        self.time = 0 
        self.followmap = collections.defaultdict(set)
        self.tweetmap = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((-self.time, tweetId))
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetmap[userId].copy()
        for followee in self.followmap[userId]:
            feed.extend(self.tweetmap[followee])

        heapify(feed)
        res = [] 
        while feed and len(res) < 10:
            res.append(heappop(feed)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
