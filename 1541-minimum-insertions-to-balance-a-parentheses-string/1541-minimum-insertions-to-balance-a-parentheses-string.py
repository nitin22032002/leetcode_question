class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        count=0
        i=0
        while(i<len(s)):
            if(s[i]=="("):
                stack.append(s[i])
                i+=1
            elif(s[i]==")"):
                if(i+1>=len(s) or s[i+1]!=")"):
                    count+=1
                    i+=1
                else:
                    i+=2
                if(len(stack)==0):
                    count+=1
                else:
                    stack.pop()
        return count+(len(stack)*2)