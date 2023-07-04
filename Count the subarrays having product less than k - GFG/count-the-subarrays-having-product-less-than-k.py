#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        ans=0
        i=j=0
        product=1
        while(j<n):
            product*=a[j]
            if(product>=k):
                t=i
                while(i<=j and product>=k):
                    product//=a[i]
                    i+=1
                r1=(min(i,j)-t)
                r2=(j-min(i,j))
                ans+=((r1)*(r1+1))//2
                ans+=(r1*r2)
            j+=1
        while(i<j and product>=k):
            product//=a[i]
            i+=1
        ans+=((j-i)*(j-i+1))//2
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