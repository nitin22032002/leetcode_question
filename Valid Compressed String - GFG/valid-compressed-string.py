#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        i=0
        j=0
        while(j<len(T)):
            while(j<len(T) and i<len(S) and not (T[j]>='0' and T[j]<='9')):
                if(S[i]!=T[j]):
                    return 0
                i+=1
                j+=1
            if(i==len(S) and j!=len(T)):return 0
            num=0
            while(j<len(T) and T[j]>='0' and T[j]<='9'):
                num=num*10+int(T[j])
                j+=1
            i+=num
            if(i>len(S)):return 0
        return int(i==len(S) and j==len(T)) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends