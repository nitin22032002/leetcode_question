class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        obj=Trie()
        nums.sort()
        queries=sorted(enumerate(queries),key=lambda x:x[1][1])
        ans=[-1 for _ in range(len(queries))]
        i=0
        j=0
        while(j<len(queries)):
            if(i<len(nums) and nums[i]<=queries[j][1][1]):
                obj.insert(nums[i])
                i+=1
            else:
                if(i!=0):
                    ans[queries[j][0]]=obj.search(queries[j][1][0])
                j+=1
        return ans
class Trie:
    def __init__(self):
        self.child={}
    def insert(self,num):
        tem=self.child
        for i in range(31,-1,-1):
            j=(num>>i)&1
            if(j not in tem):
                tem[j]={}
            tem=tem[j]
    def search(self,num):
        ans=0
        tem=self.child
        for i in range(31,-1,-1):
            t=(num>>i)&1
            # print(t,i,tem)
            if(tem.get(1-t,None)!=None):
                ans|=(1<<i)
                tem=tem[1-t]
            else:
                tem=tem[t]
        return ans
                
