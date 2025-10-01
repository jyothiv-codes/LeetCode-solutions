
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize==1 and len(hand)>0:
            return True
        hand.sort(reverse=True)
        print(hand)
        count=0
        size=0
        temp=[]
        while len(hand)>0:
            size=0
            last_node=hand.pop()
            print("last node",last_node)
            temp.append(last_node)
            size+=1
            while len(hand)>0 and last_node+1 in hand and size<groupSize:
                print("YES")
                hand.remove(last_node+1)
                last_node+=1
                temp.append(last_node)
                size+=1
            if size==groupSize:
                count+=1
                print("temp",temp)
            if size<groupSize and last_node+1 not in hand:
                return False
            #print("hand[-1]",hand[-1])
            if len(hand)>0 and hand[-1]+1 not in hand:
                return False
            temp=[]
        print(hand)
        if len(hand)==0:
            return True




        




        