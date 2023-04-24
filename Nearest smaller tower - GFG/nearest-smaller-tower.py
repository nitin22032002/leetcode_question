#User function Template for python3

class Solution:
    def nearestSmallestTower(self,arr):
        left=[-1 for _ in range(len(arr))]
        stack=[]
        for i,item in enumerate(arr):
            if(len(stack)==0 or arr[stack[-1]]<=item):
                stack.append(i)
            else:
                while(len(stack)!=0 and arr[stack[-1]]>item):
                    left[stack.pop()]=i
                stack.append(i)
        right=[-1 for _ in range(len(arr))]
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            item=arr[i]
            if(len(stack)==0 or arr[stack[-1]]<=item):
                stack.append(i)
            else:
                while(len(stack)!=0 and arr[stack[-1]]>item):
                    right[stack.pop()]=i
                stack.append(i)
        ans=[]
        # print(left,right)
        for i in range(len(arr)):
            if(left[i]!=-1 and right[i]!=-1):
                if((i-left[i])>(right[i]-i)):
                    ans.append(left[i])
                elif((i-left[i])<(right[i]-i)):
                    ans.append(right[i])
                else:
                    if(arr[left[i]]>=arr[right[i]]):
                        ans.append(right[i])
                    else:
                        ans.append(left[i])
            else:
                ans.append(max(left[i],right[i]))
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input().strip())):
        N=int(input())
        arr=[int(i) for i in input().strip().split()]
        obj=Solution()
        ans=obj.nearestSmallestTower(arr)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends