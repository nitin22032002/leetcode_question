class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.get(prices,0,k,0,{})
    def get(self,arr,i,k,prv,d):
        if(i>=len(arr)):
            if(prv!=0):
                return -10**9
            return 0
        elif(k==0 and prv==0):
            return 0
        elif((prv,i,k) not in d):
            if(prv!=0):
                d[(prv,i,k)]= max(self.get(arr,i+1,k,prv,d),self.get(arr,i+1,k,0,d)+arr[i])
            else:
                d[(prv,i,k)]= max(self.get(arr,i+1,k,prv,d),self.get(arr,i+1,k-1,1,d)-arr[i])
        return d[(prv,i,k)]