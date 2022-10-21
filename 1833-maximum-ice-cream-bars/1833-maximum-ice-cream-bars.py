class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        ans=0
        while(i<len(costs) and coins>=costs[i]):
            coins-=costs[i]
            ans+=1
            i+=1
        return ans