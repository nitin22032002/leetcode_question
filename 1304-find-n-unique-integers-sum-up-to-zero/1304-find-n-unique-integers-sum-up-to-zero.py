class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid=n//2
        i=mid
        ans=[]
        while(i>0):
            ans.append(i)
            ans.append(-i)
            i-=1
        if(len(ans)!=n):
            ans.append(0)
        return ans