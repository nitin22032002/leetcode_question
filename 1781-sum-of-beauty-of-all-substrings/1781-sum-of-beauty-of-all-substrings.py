class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            d=[0 for _ in range(26)]
            for j in range(i,len(s)):
                t=ord(s[j])-97
                d[t]+=1
                ans+=(max(d)-self.min(d))
        return ans
    def min(self,arr):
        ans=0
        for item in arr:
            if(item!=0):
                if(ans==0):
                    ans=item
                else:
                    ans=min(ans,item)
        return ans
            