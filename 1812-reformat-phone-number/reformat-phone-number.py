class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace("-","").replace(" ","")
        phone=""
        i=1
        for ch in number:
            if ch!=" " or ch!="-":
                if i==4:
                    phone+="-"
                    i=1
                phone+=ch
                i+=1
        print(phone)
        print(number)
        final_length=len(number)
        if final_length%3==1:
            phone=list(phone)
            phone[-2],phone[-3]=phone[-3],phone[-2]
            phone="".join(phone)
        return phone
        
            
            


        