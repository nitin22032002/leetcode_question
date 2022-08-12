class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b=max(x,y)
        bits=0
        while(b!=0):
            bits+=1
            b//=2
        ans=0
        for i in range(bits):
            b=1<<i
            a1=(x&b==0)
            a2=(y&b==0)
            # print(b,a1,a2)
            if(a1!=a2):
                ans+=1
        return ans