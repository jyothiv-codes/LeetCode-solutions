class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        output=[]
        def recursion(open_n,closed_n):
            if open_n==closed_n==n:
                string="".join(stack)
                output.append(string)
            if open_n<n:
                stack.append("(")
                recursion(open_n+1,closed_n)
                stack.pop()
            if closed_n<open_n:
                stack.append(")")
                recursion(open_n,closed_n+1)
                stack.pop()
        recursion(0,0)
        return output

        