class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collide=0
        
        while True:
            i=0
            collide=0
            
            while i<len(asteroids)-1 and i>=0:
                #print(i,asteroids)
                if (asteroids[i]>0 and asteroids[i+1]>0) or (asteroids[i]<0 and asteroids[i+1]<0) or (asteroids[i]<0 and asteroids[i+1]>0):
                    i+=1
                else:
                    if asteroids[i]>0 and asteroids[i+1]<0:
                        if abs(asteroids[i])>abs(asteroids[i+1]):
                            asteroids.pop(i+1)
                        elif abs(asteroids[i])<abs(asteroids[i+1]):
                            asteroids.pop(i)
                        else:
                            asteroids.pop(i)
                            asteroids.pop(i)
                            i-=1
                        collide+=1
                    else:
                        i+=1
            #print(i,asteroids)
            if collide==0:
                break
        return asteroids


        