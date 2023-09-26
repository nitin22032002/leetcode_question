#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        ans=[]
        for i in range(len(arr)):
            if(i-1>=0 and arr[i]==arr[i-1]):continue
            for j in range(i+1,len(arr)):
                if(j-1>i and arr[j]==arr[j-1]):continue
                start=j+1
                end=len(arr)-1
                while(start<end):
                    if((start-1>j and arr[start]==arr[start-1])):
                        start+=1
                        continue
                    elif((end+1<len(arr) and arr[end]==arr[end+1])):
                        end-=1
                        continue
                    s=arr[i]+arr[j]+arr[start]+arr[end]
                    if(s==k):
                        ans.append([arr[i],arr[j],arr[start],arr[end]])
                        start+=1
                    elif(s<k):
                        start+=1
                    else:
                        end-=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends