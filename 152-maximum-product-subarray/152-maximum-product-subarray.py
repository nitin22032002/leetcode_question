class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        isZero=False
        ans=(-10**9)
        i=0
        while(i<len(nums)):
            j=i
            while(j<len(nums) and nums[j]!=0):
                  j+=1
            if(j<len(nums)):
                  isZero=True
            if(j-i>0):
                ans=max(ans,self.findProduct(nums,i,j))
            i=j+1
        if(isZero):
            ans=max(ans,0)
        return ans
    def findProduct(self,arr,i,j):
        # print(i,j)
        firstNeg=1
        lastNeg=1
        product=1
        t=i
        while(i<j):
            product*=arr[i]
            i+=1
        p=1
        i=t
        # print(product)
        while(i<j):
            p*=arr[i]
            if(arr[i]<0):
                firstNeg=p
                break
            i+=1
        i=j-1
        p=1
        while(i>=t):
            p*=arr[i]
            if(arr[i]<0): 
                lastNeg=p
                break
            i-=1
        if(j-t<=1):
            return product
        else:
            return max(product,int(product/firstNeg),int(product/lastNeg))