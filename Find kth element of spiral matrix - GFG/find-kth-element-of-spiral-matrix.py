#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        startR=0
        endR=n-1
        startC=0
        endC=m-1
        while(startR<=endR or startC<=endC):
            for i in range(startC,endC+1):
                k-=1
                if(k==0):
                    return a[startR][i]
            for i in range(startR+1,endR):
                k-=1
                if(k==0):
                    return a[i][endC]
            if(startR!=endR):
                for i in range(endC,startC-1,-1):
                    k-=1
                    if(k==0):
                        return a[endR][i]
            if(startC!=endC):
                for i in range(endR-1,startR,-1):
                    k-=1
                    if(k==0):
                        return a[i][startC]
            startC+=1
            startR+=1
            endC-=1
            endR-=1
        return -1
                


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends