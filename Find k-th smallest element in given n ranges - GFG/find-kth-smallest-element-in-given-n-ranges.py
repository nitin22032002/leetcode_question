

from typing import List

class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        ranges.sort()
        ans=[]
        for val in queries:
            prv=-1
            for a,b in ranges:
                if(a<=prv):
                    a=prv+1
                # print((a,b),(val,b-a+1))
                if(val<=(b-a+1)):
                    ans.append(a+val-1)
                    break
                else:
                    prv=b
                    val-=(b-a+1)
            else:
                ans.append(-1)
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
        
        
        ranges=IntMatrix().Input(n, 2)
        
        
        q = int(input())
        
        
        queries=IntArray().Input(q)
        
        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)
        
        IntArray().Print(res)
        

# } Driver Code Ends