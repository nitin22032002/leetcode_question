#User function Template for python3


class Solution:	
	def wineSelling(self, Arr, N):
	    arr1=[]
	    arr2=[]
	    for i in range(N):
	        if(Arr[i]>0):
	            arr1.append([Arr[i],i])
	        elif(Arr[i]<0):
	            arr2.append([-Arr[i],i])
	    i=len(arr1)-1
	    j=len(arr2)-1
	    cost=0
	    while(i>=0 and j>=0):
	        if(arr1[i][0]==0):
	            i-=1
	            continue
	        elif(arr2[j][0]==0):
	            j-=1
	            continue
	        x=abs(arr1[i][1]-arr2[j][1])
	        if(arr1[i][0]>=arr2[j][0]):
	            arr1[i][0]-=arr2[j][0]
	            x*=arr2[j][0]
	            arr2[j][0]=0
	            
	        else:
	            arr2[j][0]-=arr1[i][0]
	            x*=arr1[i][0]
	            arr1[i][0]=0
	        cost+=x
	    return cost    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends