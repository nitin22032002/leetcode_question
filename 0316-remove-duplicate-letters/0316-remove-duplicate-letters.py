class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d=[0 for _ in range(26)]
        for item in s:
            j=ord(item)-97
            d[j]+=1
        stack=[]
        d1=[False for _ in range(26)]
        for item in s:
            if(len(stack)==0 or stack[-1]<=item):
                if(not d1[ord(item)-97]):
                    stack.append(item)
                d[ord(item)-97]-=1
                d1[ord(item)-97]=True
            else:
                if(not d1[ord(item)-97]):     
                    while(len(stack)!=0 and stack[-1]>item):
                        j=ord(stack[-1])-97
                        if(d[j]==0):
                            break
                        # d[ord(stack[-1])-97]+=1
                        d1[ord(stack[-1])-97]=False
                        stack.pop()
                    stack.append(item)
                d[ord(item)-97]-=1
                d1[ord(item)-97]=True
        return "".join(stack)
                
                
                