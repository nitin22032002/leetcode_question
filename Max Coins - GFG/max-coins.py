from typing import List

from bisect import bisect_left
class Solution:
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        ranges.sort()
        mar=[0]
        for item in ranges[::-1]:
            mar.append(max(mar[-1],item[2]))
        ans=0
        mar.reverse()
        # print(ranges)
        # print(mar)
        for i in range(n):
            item=ranges[i]
            r=bisect_left(ranges,[item[1],-1,-1])
            if(r<=i):
                r=i+1
            ans=max(ans,item[2]+mar[r])
        return ans
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maxCoins(n, ranges)
        
        print(res)
        

# } Driver Code Ends