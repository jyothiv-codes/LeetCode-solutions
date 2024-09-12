class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        n=int(len(s)/2)
        first=s[0:n]
        second=s[n:]
        count_first= sum(1 for char in first if char in {'a', 'e','i','o','u'})
        count_second= sum(1 for char in second if char in {'a', 'e','i','o','u'})
        if count_first==count_second:
            return True
        return False

        