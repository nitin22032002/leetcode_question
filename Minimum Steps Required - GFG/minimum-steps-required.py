class Solution:
    def minSteps(self, str : str) -> int:
        count=0
        i=0
        while(i<len(str)):
            j=i
            while(i<len(str) and str[i]==str[j]):
                i+=1
            if(i!=j):
                count+=1
        ans=0
        if(count%2==0):
            count-=1
            ans+=1
        ans+=(1+((count-1)//2))
        return ans
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends