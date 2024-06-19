class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        times=[]
        for passenger,from_,to_ in trips:
            pair1=[from_,passenger]
            pair2=[to_,-passenger]
            times.append(pair1)
            times.append(pair2)
        times.sort()
        curr=0
        for pair in times:
            curr+=pair[1]
            if curr>capacity:
                return False
        return True


        