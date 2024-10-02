class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        d={}
        for label in labels:
            d[label]=0
        combined_values=[]
        for i in range(len(values)):
            pair=[values[i],labels[i]]
            combined_values.append(pair)
        combined_values.sort(reverse=True)
        i=0
        total=0
        count=0
        while i<len(combined_values) and count<numWanted:
            value,label=combined_values[i][0],combined_values[i][1]
            if d[label]<useLimit:
                d[label]+=1
                total+=value
                i+=1
                count+=1
            else:
                i+=1
        return total
        