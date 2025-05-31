class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token in ["-","+","*","/"]:
                op1=stack.pop()
                op2=stack.pop()
                if token=="+":
                    result=op1+op2
                elif token=="-":
                    result=-op1+op2
                elif token=="*":
                    result=op1*op2
                elif token=="/":
                    
                    result=int(op2/op1)
                    
                stack.append(result)
            else:
                stack.append(int(token))
            #print(stack)
        return stack[-1]
                

        