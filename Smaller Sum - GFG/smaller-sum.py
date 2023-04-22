from typing import List


class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        tem=list(enumerate(arr))
        tem.sort(key=lambda x:[x[1],x[0]])
        ans=[0 for _ in range(n)]
        i=0
        s=0
        while(i<n):
            j=i
            r=s
            while(i<n and tem[j][1]==tem[i][1]):
                ans[tem[i][0]]=s
                r+=tem[i][1]
                i+=1
            s=r
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
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends