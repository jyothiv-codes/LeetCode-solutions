class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d={}
        if len(s)<len(target):
            return 0
        target_ind={}
        for i in s:
            d[i]=d.get(i,0)+1
        print(d)
        while True:
            flag=0
            for ch in target:
                if ch not in d:
                    flag=-1
                    print("not there")
                    return 0
                elif d[ch]<=0:
                    flag=1
                    break
                else:
                    target_ind[ch]=target_ind.get(ch,0)+1
                    d[ch]-=1
                    #print(d)
            if flag==1:
                break

        print(target_ind)
        if flag==-1:
            return 0
        if len(target_ind)>0 and sum(target_ind.values())>=len(target):
            key=min(target_ind, key=target_ind.get)

            return int(target_ind[key]/target.count(key))
        else:
            return 0
        