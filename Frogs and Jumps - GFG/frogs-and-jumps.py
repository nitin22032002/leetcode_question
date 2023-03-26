#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        d=set()
        for item in frogs:
            val=item
            if(item in d):
                continue
            while(val<=leaves):
                d.add(val)
                val+=item
        return leaves-len(d)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends