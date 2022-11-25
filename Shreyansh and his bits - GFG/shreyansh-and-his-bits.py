class Solution:
    def count (self, N):
        arr=[]
        while(N!=0):
            arr.append(N%2)
            N//=2
        arr.reverse()
        # print(arr)
        ans=self.get(arr,0)
        return ans-1
    def get(self,arr,i):
        # print("i",i)
        if(i>=len(arr)):
            return 1-arr[i-1]
        elif(arr[i]==0):
            return self.get(arr,i+1)
        else:
            c=self.count_bit(arr,i)
            ans=(self.factorial(len(arr)-i-1)//(self.factorial(c)*self.factorial(len(arr)-i-c-1)))
            ans+=self.get(arr,i+1)
            return ans
    def count_bit(self,arr,i):
        ans=0
        for i in range(i,len(arr)):
            if(arr[i]==1):
                ans+=1
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