class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if(self.check(a,b) or self.check(b,a)):
            return True
        return False
    def check(self,a,b):
        mid=len(a)//2
        if(len(a)%2==0):
            i=mid-1
            j=mid
        else:
            i=mid-1
            j=mid+1
        while(i>=0 and j<len(a)):
            if(a[i]!=a[j]):
                break
            i-=1
            j+=1
        # print(i,j)
        i1=i
        j1=j
        # print(i,j)
        status=True
        while(i>=0):
            if(a[i]!=b[j]):
                status=False
                break
            i-=1
            j+=1
        if(status):
            return True
        i=i1
        j=j1
        while(i>=0):
            if(b[i]!=a[j]):
                status=False
                break
            i-=1
            j+=1
        else:
            status=True
        return status
    