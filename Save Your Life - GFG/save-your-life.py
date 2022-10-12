#User function Template for python3


class Solution:
    def maxSum (self, w, x, b, n):
        upper=[i+65 for i in range(26)]
        lower=[i+97 for i in range(26)]
        arr=[]
        for i in range(n):
            item=x[i]
            if(item>="A" and item<='Z'):
                upper[ord(item)-65]=b[i]
            else:
                lower[ord(item)-97]=b[i]
        
        for item in w:
            if(item>='A' and item<="Z"):
                arr.append(upper[ord(item)-65])
            elif(item>='a' and item<='z'):
                arr.append(lower[ord(item)-97])
        
        if(max(arr)<0):
            m=max(arr)
            for i in range(len(arr)):
                if(m==arr[i]):
                    return w[i]
        start=-1
        end=-1
        j=0
        s=0
        maxS=0
        for i in range(len(arr)):
            s+=arr[i]
            if(s<0):
                s=0
                j=i+1
            if(maxS<=s):
                maxS=s
                start=j
                end=i
        return w[start:end+1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        w = input()
        n = int(input())
        x = input().split(' ')
        b = input().split(' ')
        for itr in range(n):
            b[itr] = int(b[itr])
       

        ob = Solution()
        print(ob.maxSum(w,x,b,n))
# } Driver Code Ends