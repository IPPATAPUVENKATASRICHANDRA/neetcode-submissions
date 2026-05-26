class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:

            # opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # closing brackets
            else:

                # stack empty
                if len(stack) == 0:
                    return False

                # matching cases
                if ch == ')' and stack[-1] == '(':
                    stack.pop()

                elif ch == '}' and stack[-1] == '{':
                    stack.pop()

                elif ch == ']' and stack[-1] == '[':
                    stack.pop()

                else:
                    return False

        return len(stack) == 0