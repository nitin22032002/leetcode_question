from typing import List


class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        i=0
        r=0
        while(i<m):
            j=i
            while(i<m and seats[i]==0):
                i+=1
            count=(i-j)
            if(count!=0):
                if(i<m):
                    count-=1
                if(j!=0):
                    count-=1
                r+=(count+1)//2
            while(i<m and seats[i]==1):i+=1
        return r>=n
        



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
        
        
        m = int(input())
        
        
        seats=IntArray().Input(m)
        
        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)
        
        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends