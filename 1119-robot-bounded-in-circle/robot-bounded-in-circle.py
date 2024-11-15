class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions=["N","W","S","E"]
        index=0
        curr_dir=directions[index]
        curr_x=0
        curr_y=0
        while True:
            for i in instructions:
                if i=="G":
                    if directions[index]=="N":
                        curr_y+=1
                    elif directions[index]=="S":
                        curr_y-=1
                    elif directions[index]=="E":
                        curr_x+=1
                    elif directions[index]=="W":
                        curr_x-=1
                elif i=="L":
                    index+=1
                    if index==4:
                        index=0

                elif i=="R":
                    index-=1
                    if index==-1:
                        index=3
            print(curr_x,curr_y,index)
            if index==0:
                return curr_x==0 and curr_y==0
           
        