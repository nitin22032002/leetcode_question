from typing import List


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        visited={}
        for item in arr:
            if(item in visited):
                visited[item]+=1
            else:
                visited[item]=1
        isOdd=False
        if(n*len(arr[0])%2!=0):
            isOdd=True
        odd=""
        for item in arr:
            if(visited[item]>0):
                visited[item]-=1
                r=item[::-1]
                if(visited.get(r,0)>0):
                    visited[r]-=1
                elif(isOdd and odd==""):
                    odd=item
                else:
                    return False
        return odd==odd[::-1]
        



#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends