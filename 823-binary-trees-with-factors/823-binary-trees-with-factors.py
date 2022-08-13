class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans=0
        arr.sort()
        d={}
        for item in arr:
            ans+=self.get(arr,item,d,set(arr))
        # print(d)
        return (ans)%((10**9)+7)
    
    def get(self,nums,target,d,arr):
        if(target==1):
            return 1
        elif((target) not in d):
            ans=0
            i=0
            while(i<len(nums) and nums[i]<=target):
                item=nums[i]
                if(target%item==0 and (target//item) in arr):
                    ans+=(self.get(nums,target//item,d,arr)*self.get(nums,item,d,arr))
                elif(target==item):
                    ans+=1
                i+=1
            d[target]=(ans)%((10**9)+7)
        return d[target]