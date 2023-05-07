class Solution:
    def stringMirror(self, str : str) -> str:
        i=1
        not_equal=-1
        while(i<len(str)):
            while(i<len(str) and str[i-1]>str[i]):i+=1
            if(i<len(str) and str[i]==str[i-1]):
                if(i-2>=0):
                    while(i<len(str) and str[i]==str[i-1]):i+=1
                else:
                    break
            else:
                break
        ans=str[:i]
        ans+=ans[::-1]
        return ans
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.stringMirror(str)
        
        print(res)
        

# } Driver Code Ends