class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1=version1.split(".")
        l2=version2.split(".")
        n1=len(l1)
        n2=len(l2)
        diff=abs(n1-n2)
        if n1<n2:
            for i in range(diff):
                l1.append("0")
        elif n2<n1:
            for i in range(diff):
                l2.append("0")
        print(l1,l2)
        i=0
        print(int('001'),int('01'))
        while i<max(n1,n2):
            if int(l1[i])==int(l2[i]):
                pass
            elif int(l1[i])>int(l2[i]):
                return 1
            else:
                return -1
            i+=1
        return 0

            


        