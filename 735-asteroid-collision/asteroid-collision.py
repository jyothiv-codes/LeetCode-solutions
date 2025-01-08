class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        total_collisions=0
        flag=0
        while flag==0:
            i=0
            this_collisions=0
            while i<len(asteroids)-1:
                if i>=0 and asteroids[i]>0 and asteroids[i+1]>0:
                    pass
                elif i>=0 and asteroids[i]<0 and asteroids[i+1]<0:
                    pass
                else:
                    
                    if i>=0 and asteroids[i]>0 and asteroids[i+1]<0:
                        #print("here",i)
                        if i>=0 and abs(asteroids[i])==abs(asteroids[i+1]) and asteroids[i]!=asteroids[i+1]:
                            asteroids.pop(i)
                            asteroids.pop(i)
                            i-=2
                        else:
                            if i>=0 and abs(asteroids[i])>abs(asteroids[i+1]):
                                asteroids.pop(i+1)
                            else:
                                asteroids.pop(i)
                            i-=1
                        this_collisions+=1
                    else:
                        
                        pass
                    
                i+=1
                #print("curr",asteroids)
            if this_collisions==0:
                break
            else:
                total_collisions+=this_collisions
        return asteroids
            

        