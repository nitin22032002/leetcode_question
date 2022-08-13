class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=list(s)
        d=[0 for _ in range(26)]
        for item in s:
            d[ord(item)-97]+=1
        i=0
        k=0
        while(i<len(order)):
            it=order[i]
            for j in range(d[ord(it)-97]):
                ans[k]=it
                k+=1
            d[ord(it)-97]=0
            i+=1
        i=0
        while(i<len(s)):
            it=s[i]
            if(d[ord(it)-97]!=0):
                for j in range(d[ord(it)-97]):
                    ans[k]=it
                    k+=1
                d[ord(it)-97]=0
            i+=1
        return "".join(ans)