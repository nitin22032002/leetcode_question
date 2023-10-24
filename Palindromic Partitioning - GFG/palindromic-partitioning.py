#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        isPal=[[False for _ in range(len(string))] for __ in range(len(string))]
        for i in range(len(string)):
            isPal[i][i]=True
        for i in range(2,len(string)+1):
            for j in range(len(string)-i+1):
                if(string[j]!=string[i+j-1]):
                    isPal[j][i+j-1]=False
                else:
                    if(i>2):
                        isPal[j][i+j-1]=isPal[j+1][i+j-2]
                    else:
                        isPal[j][i+j-1]=True
        return self.get(isPal,0,0,{})-1
    
    def get(self,isPal,i,j,dp):
        if(j>=len(isPal)):
            if(i<len(isPal)):
                return len(isPal)
            return 0
        elif((i,j) in dp):
            return dp[(i,j)]
        else:
            ans=self.get(isPal,i,j+1,dp)
            if(isPal[i][j]):
                ans=min(ans,1+self.get(isPal,j+1,j+1,dp))
            
            dp[(i,j)]=ans
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends