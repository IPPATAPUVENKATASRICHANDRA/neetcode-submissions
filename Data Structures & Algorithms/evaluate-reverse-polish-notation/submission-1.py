class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]

        for i in tokens:
            if i=='+':
                val1=stack.pop()
                val2=stack.pop()
                ans=val1+val2
                stack.append(ans)
            
            elif i=='*':
                val1=stack.pop()
                val2=stack.pop()
                ans=val1*val2
                stack.append(ans)

            elif i=='-':
                val1=stack.pop()
                val2=stack.pop()
                ans=val2-val1
                stack.append(ans)

            elif i=='/':
                val1=stack.pop()
                val2=stack.pop()
                ans=int(val2/val1)
                stack.append(ans)
            
            else:
                stack.append(int(i))
            print(stack)
        print(stack)
        return stack[0]