from typing import List

from sortedcontainers import SortedList
class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        intervals.sort(key=lambda x:[x[1],x[0]],reverse=True)
        obj=SortedList()
        for a,b in intervals:
            obj.add(a)
            j=obj.bisect_right(b)
            if(j>=k):
                return b
        return -1
        
        


        



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
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

# } Driver Code Ends