#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        start=end=-1
        ans=s=prv=0
        for i in range(n):
            if(a[i]==0):
                s+=1
            else:
                s-=1
            if(s<0):
                s=0
                prv=i+1
            if(ans<s):
                ans=s
                start=prv
                end=i
        cost=0
        for i in range(n):
            if(i>=start and i<=end):
                cost+=(1-a[i])
            else:
                cost+=a[i]
        return cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends