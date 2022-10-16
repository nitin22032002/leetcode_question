class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr=[]
        i=0
        while(i<len(nums)):
            j=i
            while(j<len(nums) and nums[j]%2==0):
                j+=1
            if(j>=len(nums)):
                arr.append(0)
            else:
                arr.append(j-i)
            i=j+1
        # print(arr)
        i=0
        c=0
        j=0
        t=0
        ans=0
        while(j<len(nums)):
            if(c==k):
                ans+=(arr[t]+1)
            if(c<=k):
                if(nums[j]%2!=0):
                    c+=1
                j+=1
            else:
                if(nums[i]%2!=0):
                    c-=1
                    t+=1
                i+=1
        while(i<len(nums) and c>k):
            if(nums[i]%2!=0):
                c-=1
                t+=1
            i+=1
        if(c==k):
            ans+=(arr[t]+1)
        return ans