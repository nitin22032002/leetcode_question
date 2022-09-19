class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def findValue(a,b):
            return abs(ord(a)-ord(b))
        arr=[findValue(s[i],t[i]) for i in range(len(s))]
        ans=0
        cost=0
        i=0
        j=0
        while(j<len(s)):
            if(cost<=maxCost):
                ans=max(ans,j-i)
                cost+=arr[j]
                j+=1
            else:
                cost-=arr[i]
                i+=1
        if(cost<=maxCost):
            ans=max(ans,j-i)
        return ans
    