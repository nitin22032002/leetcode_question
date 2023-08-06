#User function Template for python3

class Solution:
    def permutation(self,s):
        ans=[]
        self.get(list(s),0,ans)
        ans.sort()
        return ans
    
    def get(self,s,i,ans):
        if(i==len(s)-1):
            ans.append("".join(s))
        else:
            for j in range(i,len(s)):
                s[i],s[j]=s[j],s[i]
                self.get(s,i+1,ans)
                s[i],s[j]=s[j],s[i]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends