class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big #1
        self.medium=medium #2
        self.small=small #3
        

    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>0:
                self.big-=1
                return True
            else:
                return False
        elif carType==2:
            if self.medium>0:
                self.medium-=1
                return True
            else:
                return False
        elif carType==3:
            if self.small>0:
                self.small-=1
                return True
            else:
                return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)