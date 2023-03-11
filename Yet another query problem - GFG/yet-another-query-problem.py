from typing import List



class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        d={}
        for item in A:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        ans=[]
        for a,b,k in Q:
            tem={}
            for i in range(0,a):
                if(A[i] in tem):
                    tem[A[i]]+=1
                else:
                    tem[A[i]]=1
            c=0
            for i in range(a,b+1):
                t1=d[A[i]]-tem.get(A[i],0)
                if(t1==k):
                    c+=1
                if(A[i] in tem):
                    tem[A[i]]+=1
                else:
                    tem[A[i]]=1
            ans.append(c)
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
        
        N = int(input())
        
        
        num = int(input())
        
        
        A=IntArray().Input(N)
        
        
        Q=IntMatrix().Input(num, 3)
        
        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)
        
        IntArray().Print(res)
        

# } Driver Code Ends