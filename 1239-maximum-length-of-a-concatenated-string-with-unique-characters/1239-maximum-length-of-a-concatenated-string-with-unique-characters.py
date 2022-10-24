class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        return self.get(arr,0,0)
    def get(self,arr,i,bit):
        if(i>=len(arr)):
            return 0
        else:
            can_take=True
            tem=0
            for item in arr[i]:
                b=1<<(ord(item)-97)
                if(bit&b!=0 or tem&b!=0):
                    can_take=False
                    break
                tem|=b
            ans=0
            if(can_take):
                ans=self.get(arr,i+1,bit|tem)+len(arr[i])
            ans=max(ans,self.get(arr,i+1,bit))
            return ans
            