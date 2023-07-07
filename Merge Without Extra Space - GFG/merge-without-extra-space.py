#User function Template for python3
from math import ceil
class Solution:
    def merge(self,arr1,arr2,n,m):
        self.get(arr1,arr2)
    def get(self,arr1,arr2):
        i=j=0
        k=len(arr1)-1
        while(i<=k and j<len(arr2)):
            if(arr1[i]<=arr2[j]):
                i+=1
            else:
                arr1[k],arr2[j]=arr2[j],arr1[k]
                k-=1
                j+=1
        arr1.sort()
        arr2.sort()
        
    



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends