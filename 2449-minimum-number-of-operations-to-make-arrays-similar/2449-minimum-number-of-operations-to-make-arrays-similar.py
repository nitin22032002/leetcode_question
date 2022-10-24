class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        odd=[]
        even=[]
        opt=[]
        i=0
        j=0
        while(i<len(nums) and j<len(target)):
            if(nums[i]==target[j]):
                i+=1
                j+=1
            elif(nums[i]>target[j]):
                opt.append(target[j])
                j+=1
            else:
                if(nums[i]%2==0):
                    even.append(nums[i])
                else:
                    odd.append(nums[i])
                i+=1
        while(i<len(nums)):
            if(nums[i]%2==0):
                    even.append(nums[i])
            else:
                    odd.append(nums[i])
            i+=1
        s1=0
        s2=0
        while(j<len(target)):
            opt.append(target[j])
            j+=1
        ans=0
        # print(opt,even,odd)
        for item in opt:
            if(item%2==0):
                cost=abs(item-even[s1])//2
                s1+=1
            else:
                cost=abs(item-odd[s2])//2
                s2+=1
            ans+=cost
        return ans//2