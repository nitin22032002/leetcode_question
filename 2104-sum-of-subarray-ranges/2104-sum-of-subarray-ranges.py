class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            j=i
            mina,maxa=nums[i],nums[i]
            while(j<len(nums)):
                mina,maxa=min(mina,nums[j]),max(maxa,nums[j])
                ans+=(maxa-mina)
                j+=1
        return ans
                
            
class Solve:
    def __init__(self,n):
        self.arr=[[0,0] for _ in range(4*n+1)]
    
    def insert(self,start,end,arr,child):
        if(start==end):
            self.arr[child]=[arr[start],arr[start]]
            return self.arr[child]
        else:
            mid=(start+end)//2
            mina,maxa=self.insert(start,mid,arr,(2*child)+1)
            minb,maxb=self.insert(mid+1,end,arr,(2*child)+2)
            self.arr[child]=[min(mina,minb),max(maxa,maxb)]
            return self.arr[child]
        
    def get(self,start,end,i,j,child):
        if(start>=i and end<=j):
            # print((start,end))
            return self.arr[child]
        else:
            mid=(start+end)//2
            isFind=0
            if not(mid<i or start>j):
                isFind+=1
                mina,maxa=self.get(start,mid,i,j,(2*child)+1)
            if not(end<i or mid+1>j):
                isFind+=2
                minb,maxb=self.get(mid+1,end,i,j,(2*child)+2)
            if(isFind==1):
                return [mina,maxa]
            elif(isFind==2):
                return [minb,maxb]
            elif(isFind==3):
                return [min(mina,minb),max(maxa,maxb)]
            else:
                return [0,0]