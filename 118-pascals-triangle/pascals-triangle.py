class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def nCr(n,r):
            result=1
            for i in range(r):
                result=result*(n-i)
                result=result//(i+1)
            return int(result)
        final_ans=[]
        for row in range(1,numRows+1):
            temp=[]
            for col in range(1,row+1):
                value=nCr(row-1,col-1)
                temp.append(value)
            final_ans.append(temp)
            temp=[]
        return final_ans
            

        




        