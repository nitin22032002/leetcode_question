class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        d=[1,0]
        s=0
        ans=0
        mod=(10**9)+7
        for item in arr:
            s+=item
            ans+=(d[1-(s%2)])
            d[s%2]+=1
        return ans%mod