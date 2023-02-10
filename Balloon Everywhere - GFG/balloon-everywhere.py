class Solution:
    def maxInstance(self, s : str) -> int:
        d={"b":1,"a":1,"l":2,"o":2,"n":1}
        r={}
        for item in s:
            if(item in r):
                r[item]+=1
            else:
                r[item]=1
        ans=len(s)
        for item in d:
            if(r.get(item)>=d[item]):
                if(d[item]==2):
                    ans=min(ans,((r[item]//2)))
                else:
                    ans=min(ans,(r[item]))
            else:
                return 0
        return ans


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.maxInstance(s)
        
        print(res)

# } Driver Code Ends