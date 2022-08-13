class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans=0
        arr.sort()
        d={}
        for item in arr:
            ans+=self.get(set(arr),item,d)
        # print(d)
        return (ans)%((10**9)+7)
    
    def get(self,nums,target,d):
        if(target==1):
            return 1
        elif((target) not in d):
            ans=0
            for item in nums:
                if(target%item==0 and (target//item) in nums):
                    ans+=(self.get(nums,target//item,d)*self.get(nums,item,d))
                elif(target==item):
                    ans+=1
                # else:
                #     print(target,item)
                
            d[target]=(ans)%((10**9)+7)
        return d[target]