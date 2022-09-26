class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if(k%2==0):
            return -1
        else:
            x=len((str(k)))
            n=int(x*"1")
            arr=[False for _ in range(k)]
            count=x
            while(n%k!=0 and not arr[n%k]):
                arr[n%k]=True
                # print(n%k)
                n*=10
                n+=1
                count+=1
            if(n%k!=0):
                return -1
            return count