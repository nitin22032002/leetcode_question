class Solution:
    def maxLength(self, arr: List[str]) -> int:
        t=[]
        for item in arr:
            bit=0
            for ch in item:
                j=ord(ch)-97
                b=1<<j
                if(b&bit!=0):
                    break
                bit|=b
            else:
                t.append([bit,item])
        return self.get(t,0,0,{})
    def get(self,arr,i,bit,dp):
        if(i>=len(arr)):
            return 0
        elif((i,bit) in dp):
            return dp[(i,bit)]
        else:
            can_take=True
            for j in range(26):
                b=1<<j
                if(bit&b!=0 and arr[i][0]&b!=0):
                    can_take=False
                    break
            ans=0
            if(can_take):
                ans=self.get(arr,i+1,bit|arr[i][0],dp)+len(arr[i][1])
            ans=max(ans,self.get(arr,i+1,bit,dp))
            return ans
            