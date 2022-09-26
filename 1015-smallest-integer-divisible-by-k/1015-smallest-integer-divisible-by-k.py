class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if(k%2==0):
            return -1
        else:
            n=1
            s=set()
            count=1
            while(n%k!=0 and n%k not in s):
                s.add(n%k)
                n*=10
                n+=1
                count+=1
            if(n%k!=0):
                return -1
            return count