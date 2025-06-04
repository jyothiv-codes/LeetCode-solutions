class ThroneInheritance:

    def __init__(self, kingName: str):
        self.order=[]
        self.d={}
        self.d[kingName]=[]
        self.alive={kingName:True}
        self.start=kingName

        

    def birth(self, parentName: str, childName: str) -> None:
        self.d[childName]=[]
        self.alive[childName]=True

        if parentName in self.d:
            self.d[parentName].append(childName)

    def death(self, name: str) -> None:
        self.alive[name]=False

    def getInheritanceOrder(self) -> List[str]:
        def add_to_inheritance(start,inheritance,alive):
            if not self.alive[start]:
                pass
            else:
                inheritance.append(start)
            for child in self.d[start]:
                add_to_inheritance(child,inheritance,alive)
        inheritance=[]
        add_to_inheritance(self.start,inheritance,self.alive)
        return inheritance
    
    
        
        

        
class Person:
    def __init__(self, name,parent):
        self.name = name
        self.parent = parent
        self.alive=True


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()