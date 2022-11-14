#User function Template for python3
from bisect import bisect_right
class Solution:
    def numberOfSubsequences (self,S,W):
        arr=[[] for _ in range(26)]
        for i in range(len(S)):
            arr[ord(S[i])-97].append(i)
        # print(arr)
        ans=0
        visited=[False for _ in range(len(S))]
        for item in arr[ord(W[0])-97]:
            start=item
            if(visited[start]):
                continue
            j=1
            while(j<len(W)):
                val=W[j]
                a=arr[ord(val)-97]
                ind=bisect_right(a,start)
                # print(ind,a)
                if(ind==len(a)):
                    return ans
                ind=a[ind]
                if(visited[ind]):
                    start=ind
                    continue
                visited[ind]=True
                start=ind
                j+=1
            ans+=1
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends