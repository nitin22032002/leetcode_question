class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        m=max(nums)
        bits=0
        while(m!=0):
            bits+=1
            m//=2
        d=[[0,0] for _ in range(bits)]
        for i in range(bits):
            b=1<<i
            for j in range(len(nums)):
                bit=int((nums[j]&b)!=0)
                d[i][bit]+=1
        ans=0
        # print(d)
        for i in range(bits):
            ans+=(d[i][0]*d[i][1])
        return ans