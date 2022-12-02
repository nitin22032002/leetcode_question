#User function Template for python3

class Solution:
    def isItPossible(sef, S, T, M, N):
        i=0
        j=0
        while(i<len(T)):
            if(T[i]=='A'):
                while(j<len(S)):
                    if(S[j]=='B'):
                        return 0
                    elif(S[j]=='A'):
                        j+=1
                        break
                    j+=1
                else:
                    return 0
            elif(T[i]=='B'):
                while(j<=i):
                    if(S[j]=='A'):
                        return 0
                    elif(S[j]=='B'):
                        j+=1
                        break
                    j+=1
                else:
                    return 0
            i+=1
        # print((i,j))
        while(j<len(S) and S[j]=='#'):
            j+=1
        if(len(T)==i and j==len(S)):
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S,T=input().split()
        ob=Solution()
        print(ob.isItPossible(S,T,len(S),len(T)))
# } Driver Code Ends