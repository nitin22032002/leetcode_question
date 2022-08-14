class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if(n==0):return 1
        nums=[9]*n
        ans=0
        d={}
        for i in range(nums[0]+1):
            if(i==0):
                bit=0
            else:
                bit=1<<i
            if(i==nums[0] and len(nums)>1):
                ans+=self.get(nums,1,nums[1],bit,d)
            else:
                ans+=self.get(nums,1,10,bit,d)
        return ans
    
    def get(self,nums,i,end,bits,d):
        if(i>=len(nums)):
            return 1
        elif((i,bits,end) in d):
            return d[(i,bits,end)]
        else:
            ans=0
            if(end==10):
                last=10
            else:
                last=end+1
            for j in range(last):
                b=1<<j
                if(j==0 and bits==0):
                    if((nums[i]==end and end==j) and i!=len(nums)-1):
                        ans+=self.get(nums,i+1,nums[i+1],bits,d)
                    else:
                        ans+=self.get(nums,i+1,10,bits,d)
                elif(bits&b==0):
                    if((end==j) and i!=len(nums)-1):
                        ans+=self.get(nums,i+1,nums[i+1],bits|b,d)
                    else:
                        ans+=self.get(nums,i+1,10,bits|b,d)
            d[(i,bits,end)]=ans
            return ans