from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        count=0
        for i in range(n//2):
            if(arr[i]!=arr[n-i-1]):count+=1
        ans=(count//2)+(count%2)
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
        res = obj.bitMagic(n, arr)
        
        print(res)
        

# } Driver Code Ends