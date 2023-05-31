class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pars = {")":"(","}":"{","]":"["}
        for x in s:
            if x in {"(","{","["}:
                stack.append(x)
            else:
                if stack==[] or (stack[-1]!=pars[x]):
                    return False
                else:
                    stack.pop()
        return stack==[]

