from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        ans=[]
        i=0
        s=0
        j=0
        r=0
        while(j<n):
            s+=a[j]
            prv=(i*a[i])-r
            next=(s-r)-(j-i+1)*a[i]
            d=prv+next
            t=i+1
            if(t<=j):
                prv=(t*a[t])-(r+a[t-1])
                next=(s-r-a[t-1])-(j-t+1)*a[t]
                # print(t,prv,next,j)
            while(t<=j and prv+next<=d):
                r+=a[t-1]
                d=prv+next
                t+=1
                if(t>j):break
                prv=(t*a[t])-(r+a[t-1])
                next=(s-r-a[t-1])-(j-t+1)*a[t]
            i=t-1
            ans.append(d)
            # print(i)
            j+=1
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
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        res = obj.optimalArray(n, a)
        
        IntArray().Print(res)
        

# } Driver Code Ends