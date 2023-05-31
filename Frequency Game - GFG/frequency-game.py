#User function Template for python3


def LargButMinFreq(arr,n):
    d={}
    for item in arr:
        if(item in d):
            d[item]+=1
        else:
            d[item]=1
    ans=-1
    fre=1e9
    for item in d:
        if(d[item]<fre):
            fre=d[item]
            ans=item
        elif(d[item]==fre):
            ans=max(ans,item)
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends