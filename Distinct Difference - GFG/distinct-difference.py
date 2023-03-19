from typing import List


class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        d={}
        for item in A:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        tem=set()
        ans=[]
        for item in A:
            d[item]-=1
            if(d[item]==0):
                del d[item]
            ans.append(len(tem)-len(d))
            tem.add(item)
        return ans
        



#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends