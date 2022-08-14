class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        nums=list(zip(difficulty,profit))
        nums.sort()
        # obj=Tree(nums)
        maximize=[0]
        for item in nums:
            maximize.append(max(maximize[-1],item[1]))
        profit=0
        for item in worker:
            i=self.find(nums,item)
            profit+=maximize[i+1]
        return profit
                
    def find(self,nums,target):
        start=0
        end=len(nums)-1
        while(start<end-1):
            mid=(start+end)//2
            if(nums[mid][0]<=target):
                start=mid
            else:
                end=mid
        if(nums[end][0]<=target):
            return end
        elif(nums[start][0]<=target):
            return start
        else:
            return -1
        


class Tree:
    def __init__(self,nums):
        self.arr=[0 for _ in range(4*len(nums))]
        self.set(nums,0,len(nums)-1,0)
    def set(self,nums,start,end,child):
        if(start==mid):
            self.arr[child]=nums[start][1]
            return self.arr[child]
        else:
            mid=(start+end)//2
            s=0
            s+=self.set(nums,start,mid,(2*child)+1)
            s+=self.set(nums,mid+1,end,(2*child)+2)
            self.arr[child]=s
            return s
        
    def get(self,start,end,i,j,child):
        if(i<=start and j>=end):
            return self.arr[child]
        elif(end<i or start>j):
            return 0
        else:
            mid=(start+end)//2
            return self.get(start,mid,i,j,(2*child)+1)+self.get(mid+1,end,i,j,(2*child)+2)
            
        