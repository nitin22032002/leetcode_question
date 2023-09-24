class Solution:
    def duplicates(self, arr, n): 
        d={}
        for item in arr:
            if(item in d):d[item]+=1
            else:d[item]=1
        ans=[]
        for i in range(n):
            if(d.get(i,0)>1):ans.append(i)
        if(len(ans)==0):return [-1]
        return ans
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends