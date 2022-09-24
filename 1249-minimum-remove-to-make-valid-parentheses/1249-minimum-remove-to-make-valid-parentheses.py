class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        # print(s)
        stack=[]
        for i in range(len(s)):
            if(s[i]!="(" and s[i]!=")"):
                continue
            elif(s[i]=="("):
                stack.append(i)
            else:
                if(len(stack)==0):
                    s[i]=""
                else:
                    stack.pop()
        for item in stack:
            s[item]=""
        return "".join(s)
            