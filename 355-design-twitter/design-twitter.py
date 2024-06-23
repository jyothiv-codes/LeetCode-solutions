class Twitter(object):

    def __init__(self):
        self.tweets={}
        self.follows={}
        self.timestamp=0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append([self.timestamp,tweetId])
        self.timestamp+=1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        tweets_return=[]
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                if tweet not in tweets_return:
                    tweets_return.append(tweet)
        if userId in self.follows:
            for user in self.follows[userId]:
                if user in self.tweets:
                    for tweet in self.tweets[user]:
                        if tweet not in tweets_return:
                            tweets_return.append(tweet)

        tweets_return.sort(reverse=True)
        print(tweets_return)
        return [tweet[1] for tweet in tweets_return[:10]]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.follows:
            self.follows[followerId]=[]
        self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)