#User function Template for python3

class Solution:
    def satisfyEqn(self, a, n):
        d={}
        for i in range(n):
            for j in range(i+1,n):
                s=a[i]+a[j]
                if(s in d):
                    arr=d[s]
                    if(len(arr)==2):
                        if(i!=arr[0] and i!=arr[1] and j!=arr[0] and j!=arr[1]):
                            arr.extend([i,j])
                else:
                    d[s]=[i,j]
        # print(d)
        arr=[]
        for item in d.values():
            if(len(item)==4):
                arr.append(item)
        if(len(arr)==0):
            return [-1]*4
        arr.sort()
        return arr[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        ptr=ob.satisfyEqn(A,N)
        print(*ptr)
# } Driver Code Ends