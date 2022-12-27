#User function Template for python3



def maxArea(A,le):
    ans=0
    start=0
    end=le-1
    while(start<end):
        m=min(A[start],A[end])
        ans=max(ans,m*(end-start))
        if(A[start]<A[end]):
            start+=1
        else:
            end-=1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends