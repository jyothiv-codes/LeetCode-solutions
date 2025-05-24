class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        length=len(flowerbed)
        if length==1 and flowerbed[i]==0:
            return True
        while n>0:
            while i<length and n>0:
                if flowerbed[i]==0:
                    # check if flower can be placed
                    if i-1>=0 and i+1<length:
                        if flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                            flowerbed[i]=1
                            n-=1
                    if i==0:
                        if i+1<length and flowerbed[i+1]!=1:
                            flowerbed[i]=1
                            n-=1
                    if i==length-1:
                        if i-1>=0 and flowerbed[i-1]!=1:
                            flowerbed[i]=1
                            n-=1

                i+=1
            if i==len(flowerbed):
                break
        print(flowerbed,n)
        if n==0:
            return True
        return False


        