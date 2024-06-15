class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        def mask_email(string):
            string=string.lower()
            i=1
            while string[i]!="@":
                i+=1
            string=string[0]+"*****"+string[i-1:]
            return string
        def mask_phone(string):
            if "(" in string:
                string=string.replace("(","")
            if ")" in string:
                string=string.replace(")","")
            if "+" in string:
                string=string.replace("+","")
            if "-" in string:
                string=string.replace("-","")
            string=string.replace(" ","")
            print(string)
            if len(string)==10:
                return "***-***-"+string[-4:]
            elif len(string)==11:
                return "+*-***-***-"+string[-4:]
            elif len(string)==12:
                return "+**-***-***-"+string[-4:]
            elif len(string)==13:
                return "+***-***-***-"+string[-4:]


        if "@" in s:
            answer=mask_email(s)
        else:
            answer=mask_phone(s)
        return answer
        
        