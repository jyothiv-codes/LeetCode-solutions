import heapq as hp
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        m=0
        for ch in s:
            d[ch]=d.get(ch,0)+1
            m=max(m,d[ch])
        
        sorted_l = list(sorted(d.items(), key=lambda item: item[1], reverse=True))   
        

        #create a heap
        heap=[]
        for pair in sorted_l:
            create_pair=[pair[1]*(-1),pair[0]]
            heap.append(create_pair)
        hp.heapify(heap)
        ans=""
        temp_arr=[]
        while len(heap)>0:
            print(heap,"heap at every step")
            temp=hp.heappop(heap)
            if ans=="" or temp[1]!=ans[-1]:
                print("going thru if")
                ans+=temp[1]
                temp[0]+=1
                if temp[0]*(-1)>0:
                    hp.heappush(heap,temp)
                
            else:
                print("going thru else")
                temp_arr.append(temp)
                while temp[1]==ans[-1] and len(heap)>0:
                    print("Within while")
                    temp=hp.heappop(heap)
                    temp_arr.append(temp)
                if temp[1]==ans[-1]:
                    print("if within else")
                    return ""
                else:
                    print("else within else")
                    ans+=temp[1]
                    temp[0]+=1
                    if temp[0]>0:
                        hp.heappush(heap,temp)
                    while len(temp_arr)>0:
                        pair=temp_arr.pop()
                        if pair[0]<0:
                            hp.heappush(heap,pair)
                    print("heap after else within else",heap)
                print("at the end of else, the heap is ",heap)

                
                        

                

        print(heap)
        

        return ans

        