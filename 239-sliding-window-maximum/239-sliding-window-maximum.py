class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        j=0
        while(j<k):
            if(len(stack)==0 or stack[-1][0]>=nums[j]):
                stack.append([nums[j],j])
            else:
                while(len(stack)!=0 and stack[-1][0]<nums[j]):
                    stack.pop()
                stack.append([nums[j],j])
            j+=1
        k=0
        ans=[]
        # ans=[-1 for _ in range(len(nums)-k+1)]
        # print(len(ans))
        i=-1
        while(j<len(nums)):
            i+=1
            if(stack[k][1]<i):
                k+=1
            ans.append(stack[k][0])
            if(len(stack)==(k) or stack[-1][0]>=nums[j]):
                stack.append([nums[j],j])
            else:
                while(len(stack)!=(k) and stack[-1][0]<nums[j]):
                    stack.pop()
                stack.append([nums[j],j])
            j+=1
        i+=1
        if(stack[k][1]<i):
            k+=1
        ans.append(stack[k][0])
        return ans