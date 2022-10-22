class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if(len(prices)<2):
            return 0
        start=prices[0]
        cost=0
        for i in range(1,len(prices)):
            if(start>prices[i]):
                start=prices[i]
            elif(prices[i]>=(fee+start)):
                cost+=(prices[i]-fee-start)
                start=prices[i]-fee
        return cost