class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        mid=len(nums)//2
        i=0
        j=mid
        k=0
        ans=[]
        while(k<len(nums)):
            if(k%2==0):
                ans.append(nums[j])
                j+=1
            else:
                ans.append(nums[i])
                i+=1
            k+=1
        # print(ans)
        for i in range(len(nums)):
            nums[i]=ans[i]
        