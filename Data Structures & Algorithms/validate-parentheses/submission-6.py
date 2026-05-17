class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: ##elif evaluates only one
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif not stack or stack.pop() != c: 
                return False
        return not stack



        

##for each open bracket, i pop in the stack
##for each closed bracket, i will check the top of stack if same type
##return true if empty stack