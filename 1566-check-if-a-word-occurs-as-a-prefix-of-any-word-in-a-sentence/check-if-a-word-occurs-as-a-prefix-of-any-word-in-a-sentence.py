class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        i=1
        for word in words:
            if searchWord in word[0:len(searchWord)]:
                return i
            i+=1
        return -1

        