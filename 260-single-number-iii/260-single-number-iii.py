class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for item in nums:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        ans=[None,None]
        for item in d:
            if(d[item]==1):
                if(ans[0]==None):
                    ans[0]=item
                else:
                    ans[1]=item
                    return ans
        