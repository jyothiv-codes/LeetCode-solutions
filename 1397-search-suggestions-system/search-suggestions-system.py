class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d={}
        
        for product in products:
            s=""
            for ch in product:
                s+=ch
                if s not in d:
                    d[s]=[]
                d[s].append(product)

        #print(d)
        search=""
        output=[]
        for ch in searchWord:
            search+=ch
            if search in d:
                d[search].sort()
                output.append(d[search][:3])
            else:
                output.append([])
        return output 

        