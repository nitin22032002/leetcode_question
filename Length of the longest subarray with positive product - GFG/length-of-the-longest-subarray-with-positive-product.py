#User function Template for python3


class Solution:
    def maxLength(self,arr,n):
        l=r=-1
        ans=i=j=p=0
        while(j<n):
            if(arr[j]==0):
                # print((i,j,l,r))
                if(p%2==0):
                    ans=max(ans,j-i)
                else:
                    ans=max(ans,j-l-1,r-i)
                l=r=-1
                p=0
                i=j+1
            else:
                if(arr[j]<0):
                    p+=1
                    if(l==-1):
                        l=j
                    r=j
            j+=1
        if(p%2==0):
            ans=max(ans,j-i)
        else:
            ans=max(ans,j-l-1,r-i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.maxLength(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends