#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        ans=[]
        for item in Dictionary:
            i=0
            for val in item:
                if(val>='A' and val<='Z'):
                    if(i>=len(Pattern) or Pattern[i]!=val):break
                    i+=1
            if(i>=len(Pattern)):
                ans.append(item)
        if(len(ans)==0):
            return ["-1"]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends