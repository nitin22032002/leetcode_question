class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        ans=0
        stack=[]
        i=0
        n=len(properties)
        while(i<n):
            j=i
            while(j<n and properties[j][0]==properties[i][0]):
                j+=1
            t=j-1
            if(len(stack)==0 or stack[-1]>=properties[t][1]):
                stack.append(properties[t][1])
            else:
                while(len(stack)!=0 and stack[-1]<properties[t][1]):
                    ans+=1
                    stack.pop()
                stack.append(properties[t][1])
            t-=1
            while(t>=i):
                stack.append(properties[t][1])
                t-=1
            i=j
        return ans