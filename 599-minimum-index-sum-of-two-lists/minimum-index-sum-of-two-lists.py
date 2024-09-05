class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        i=0
        d={}
        for word in list1:
            if word in list2:
                d[word]=d.get(word,0)+i+list2.index(word)
            i+=1
        print(d)
        m=min(d.values())
        output=[]
        for key in d:
            if d[key]==m:
                output.append(key)
        return output

        