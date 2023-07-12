#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        mod=int(1e9+7)
        start=N
        ans=1
        while(R>0):
            if(R&1==1):
                ans*=start
                ans%=mod
            start*=start
            start%=mod
            R>>=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends