from typing import List


class Solution:
    def goodSubsets(self, n : int, arr : List[int]) -> int:
        primes=[2,3,5,7,11,13,17,19,23,29]
        updated=[]
        for item in arr:
            r=0
            j=0
            while(j<len(primes)):
                if(item%primes[j]==0 and (r>>j)&1==0):
                    item//=primes[j]
                    r|=(1<<j)
                elif(item%primes[j]!=0):
                    j+=1
                else:
                    break
            else:
                updated.append(r)
        temp={}
        count=0
        for item in updated:
            if(item==0):
                count+=1
                continue
            if(item in temp):
                temp[item]+=1
            else:
                temp[item]=1
        updated=list(temp.items())
        ans=self.get(updated,0,0,{})
        mod=int(1e9+7)
        ans*=(pow(2,count,mod))
        return ans%mod
    def get(self,arr,i,bit,dp):
        if(i>=len(arr)):
            if(bit==0):return 0
            return 1
        elif((i,bit) in dp):
            return dp[(i,bit)]
        else:
            ans=self.get(arr,i+1,bit,dp)
            if((bit|arr[i][0])==(bit^arr[i][0])):
                ans+=self.get(arr,i+1,bit|arr[i][0],dp)*arr[i][1]
            ans%=int(1e9+7)
            dp[(i,bit)]=ans
            return ans
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.goodSubsets(n, arr)
        
        print(res)
        

# } Driver Code Ends