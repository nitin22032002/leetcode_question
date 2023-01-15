#User function Template for python3

from sortedcontainers import SortedList
class Solution():
    def countSubstring(self, S):
        r=0
        obj=SortedList()
        obj.add(0)
        ans=0
        for i in range(len(S)):
            if(S[i]=='1'):
                r+=1
            else:
                r-=1
            j=obj.bisect_left(r)
            obj.add(r)
            ans+=j
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends