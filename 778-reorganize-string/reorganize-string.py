import heapq as hp
class Solution:
    def reorganizeString(self, s: str) -> str:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        sorted_l=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
        heap=[]
        for pair in sorted_l:
            to_add=[pair[1]*(-1),pair[0]]
            heap.append(to_add)
        hp.heapify(heap)
        ans=""
        temp_arr=[]
        while len(heap)>0:
            temp=hp.heappop(heap)
            # if ans is null or prev char doesn't match the char at temp
            if ans=="" or ans[-1]!=temp[1]:
                ans+=temp[1]
                temp[0]+=1
                if temp[0]*(-1)>0:
                    hp.heappush(heap,temp)
            #else
            else:
                temp_arr.append(temp)
                while temp[1]==ans[-1] and len(heap)>0:
                    temp=hp.heappop(heap)
                    temp_arr.append(temp)
                if temp[1]==ans[-1]:
                    return ""
                else:
                    ans+=temp[1]
                    temp[0]+=1
                    if temp[0]>0:
                        hp.heappush(heap,temp)
                    while len(temp_arr)>0:
                        pair=temp_arr.pop()
                        if pair[0]<0:
                            hp.heappush(heap,pair)
        return ans
                    
                






        