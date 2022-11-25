class Solution:
    def count (self, N):
        arr=[]
        c=0
        while(N!=0):
            arr.append(N%2)
            c+=(N%2)
            N//=2
        arr.reverse()
        # print(arr)
        ans=self.get(arr,0,c)
        return ans-1
    def get(self,arr,i,c):
        if(i>=len(arr)):
            return 1-arr[i-1]
        elif(arr[i]==0):
            return self.get(arr,i+1,c)
        else:
            ans=(self.factorial(len(arr)-i-1)//(self.factorial(c)*self.factorial(len(arr)-i-c-1)))
            ans+=self.get(arr,i+1,c-1)
            return ans
    def factorial(self,n):
        # print(n)
        ans=1
        for i in range(1,n+1):
            ans*=i
        return ans
        



#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        print(ob.count(N))



# } Driver Code Ends