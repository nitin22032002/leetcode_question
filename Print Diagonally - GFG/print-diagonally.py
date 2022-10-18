#User function Template for python3

def downwardDigonal(n, arr): 
    ans=[]
    si=0
    sj=0
    while(si<n):
        i=si
        j=sj
        while(i<n and j>=0):
            # print((i,j))
            ans.append(arr[i][j])
            i+=1
            j-=1
        if((sj+1)<n):
            sj+=1
            si=0
        else:
            si+=1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends