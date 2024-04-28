class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for ch in s:
            if ch=="(" or ch=="[" or ch=="{":
                stack.append(ch)
            else:
                if len(stack)>0:
                    if ch==")":
                        end=stack.pop()
                        if end!="(":
                            return False
                    elif ch=="]":
                        end=stack.pop()
                        if end!="[":
                            return False
                    elif ch=="}":
                        end=stack.pop()
                        if end!="{":
                            return False
                else:
                    return False
        if len(stack)==0:
            return True
        return False
                    
        