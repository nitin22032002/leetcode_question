class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven=0
        for item in nums:
            if(item&1==0):
                sumEven+=item
        ans=[]
        # print(sumEven)
        for item in queries:
            val,index=item
            oddVal=nums[index]
            if(oddVal&1==0):
                if((oddVal+val)&1==0):
                    sumEven+=val
                else:
                    sumEven-=oddVal
            else:
                if((oddVal+val)&1==0):
                    sumEven+=(oddVal+val)
            nums[index]+=val
            ans.append(sumEven)
        return ans