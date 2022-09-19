class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def findValue(a,b):
            return abs(ord(a)-ord(b))
        ans=0
        cost=0
        i=0
        j=0
        while(j<len(s)):
            if(cost<=maxCost):
                ans=max(ans,j-i)
                cost+=findValue(s[j],t[j])
                j+=1
            else:
                cost-=findValue(s[i],t[i])
                i+=1
        if(cost<=maxCost):
            ans=max(ans,j-i)
        return ans
    