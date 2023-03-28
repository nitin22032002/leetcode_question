#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Shop:
    chocolates=[]
    countOfCalls=0
    def __init__(self):
        self.chocolates=[]
        self.countOfCalls=0
    def addChocolate(self,price):
        self.chocolates.append(price)
    def get(self,i):
        self.countOfCalls+=1
        if (self.countOfCalls>50 or i>=len(self.chocolates) or i<0):
            return -1
        return self.chocolates[i]


# } Driver Code Ends
#User function Template for python3

"""
Instructions - 

    1. 'shop' is object of class Shop.
    2. User 'shop.get(int i)' to enquire about the price
            of the i^th chocolate.
    3. Every chocolate in shop is arranged in increasing order
            i.e. shop.get(i) <= shop.get(i + 1) for all 0 <= i < n - 1
"""

from sortedcontainers import SortedList
class Solution:
    shop=Shop()
    def __init__(self,shop):
        self.shop=shop
    
    def find(self,n,k):
        obj=SortedList()
        ans=0
        mi=self.shop.get(0)
        arr=[]
        start=0
        end=n-1
        while(k>=mi):
            while(start<end-1):
                mid=(start+end)//2
                c=self.shop.get(mid)
                # print(c)
                if(k==c):
                    ans+=1
                    return ans
                elif(k>c):
                    start=mid
                else:
                    end=mid-1
                obj.add([c,mid])
            c=self.shop.get(end)
            # print(c,k)
            if(c<=k):
                ans+=(k//c)
                k=k%c
            else:
                c=self.shop.get(start)
                ans+=(k//c)
                k=k%c
            j1=obj.bisect_right([k,-1])
            if(j1==0 and len(obj)!=0 and  obj[j1][0]!=k):
                start=0
                if(j1>len(obj)):
                    end=obj[j1][1]
            elif(j1<len(obj) and obj[j1][0]==k):
                start=obj[j1][1]
                end=obj[j1][1]
            elif(len(obj)!=0):
                start=obj[j1-1][1]
                if(j1>len(obj)):
                    end=obj[j1][1]
            else:
                start=0
        return ans

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        shop=Shop()
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        for choco in arr:
            shop.addChocolate(choco)
        ob = Solution(shop)
        ans = ob.find(n, k)
        print(ans)
        tc -= 1
        

        
# } Driver Code Ends