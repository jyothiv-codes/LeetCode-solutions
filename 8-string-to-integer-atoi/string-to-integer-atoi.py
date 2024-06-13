class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        integer=""
        negative=False
        positive=True
        positive_set=False
        power=0
        prev=""
        for ch in s:
            if ch==" ":
                if negative is True or positive_set is True:
                    break
                elif integer!="":
                    break
                else:
                    pass
            elif ch==" " and integer!="":
                print("break")
                break
            elif ch=="-" and prev=="":
                if negative is True:
                    break
                else:
                    negative=True
            elif ch=="+" and prev=="":
                if positive_set is True:
                    break
                else:
                    positive_set=True
            elif ch in ["0","1","2","3","4","5","6","7","8","9"]:
                if ch=="0":
                    if prev==" ":
                        pass
                    else:
                        integer+=ch
                else:
                    integer+=ch
                prev=ch
            else:
                break
        print(integer)
        finalans=0
        if negative is True and positive_set is True:
            return 0
        for ch in integer[::-1]:
            finalans+=((10**power)*int(ch))
            power+=1
        if negative is True and finalans>=(2**31):
            finalans=-(2**31)  
            return finalans
        elif positive is True and finalans>=((2**31)-1):
            finalans=2**31-1
            print("positive")
        if negative:
            return -finalans
        return finalans

        
                

        