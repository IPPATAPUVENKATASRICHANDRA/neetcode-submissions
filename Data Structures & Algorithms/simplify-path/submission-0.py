class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split('/')
        print(paths)

        for i in paths:

            print(stack)
            if i=='..':
                if stack:
                    stack.pop()
                else:
                    continue
            elif i!='' and i!='.':
                stack.append(i)

        return '/'+'/'.join(stack)