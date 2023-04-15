from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        d=set([arr[0]])
        ans=0
        for i in range(1,len(arr)):
            if(arr[i] in d):
                ans+=time[arr[i]-1]-1
            ans+=1
            d.add(arr[i])
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
        
        
        time=IntArray().Input(n)
        
        obj = Solution()
        res = obj.totalTime(n, arr, time)
        
        print(res)
        

# } Driver Code Ends