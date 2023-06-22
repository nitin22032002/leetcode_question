#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        count1=0
        count2=0
        for item in bills:
            if(item==5):count1+=1
            else:
                if(count1==0):
                    return False
                elif(item==10):
                    count2+=1
                    count1-=1
                else:
                    if(count2>0):
                        count2-=1
                        count1-=1
                    else:
                        if(count1>=3):
                            count1-=3
                        else:return False
        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends