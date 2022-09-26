class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if(k%2==0):
            return -1
        else:
            x=len((str(k)))
            n=int(x*"1")
            s=set()
            count=x
            while(n%k!=0 and n%k not in s):
                s.add(n%k)
                # print(n%k)
                n*=10
                n+=1
                count+=1
            if(n%k!=0):
                return -1
            return count