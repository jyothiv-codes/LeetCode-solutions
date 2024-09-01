import random
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==1:
            if s[0]=="?":
                return "a"
            else:
                return s
        final=""
        place=""
        string="abcdefghijklmnopqrstuvwxyz"
        letters=[ch for ch in string]
        for i in range(len(s)):
            if s[i]=="?":
                if i==0 or i==len(s)-1:
                    compare_ch=s[1]
                    if compare_ch=="z":
                        place="a"
                    else:
                        place=random.choice(letters)
                        if place!=compare_ch:
                            pass
                        else:
                            while place==compare_ch:
                                place=random.choice(letters)
                else:
                    prev_ch=final[i-1]
                    next_ch=s[i+1]
                    place=random.choice(letters)
                    if place!=prev_ch and place!=next_ch:
                        pass
                    else:
                        while place==prev_ch or place==next_ch:
                            place=random.choice(letters)
                final+=place
            else:
                final+=s[i]
        return final
            

        