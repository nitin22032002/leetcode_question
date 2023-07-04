#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        ans=0
        i=j=0
        product=1
        while(j<n):
            product*=a[j]
            while(i<=j and product>=k):
                product//=a[i]
                i+=1
            j+=1
            ans+=(j-i)
        return ans
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends