class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        print(sorted_boxes)
        curr=0
        i=0
        units=0
        while curr<truckSize and i<len(sorted_boxes):
            diff=(truckSize-curr)
            if sorted_boxes[i][0]<diff:
                curr+=sorted_boxes[i][0]
                units+=(sorted_boxes[i][1]*sorted_boxes[i][0])
            else:
                curr+=diff
                units+=(sorted_boxes[i][1]*diff)

            i+=1
            
        return units

            
        