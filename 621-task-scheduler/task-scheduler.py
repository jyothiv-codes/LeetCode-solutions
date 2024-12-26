from collections import OrderedDict, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
        freq = Counter(tasks)
        d = OrderedDict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        max_freq=max(d.values())
        max_count=0
        for key in d:
            if d[key]==max_freq:
                max_count+=1
        return max(len(tasks),(max_freq-1)*(n+1)+max_count)
        