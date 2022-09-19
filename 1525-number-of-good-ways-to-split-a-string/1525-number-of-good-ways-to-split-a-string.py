class Solution:
    def numSplits(self, s: str) -> int:
        index=[0 for _ in range(26)]
        c2=0
        b2=0
        for i in range(len(s)):
            j=ord(s[i])-97
            index[j]=i
            b=1<<j
            if(b&b2==0):
                c2+=1
            b2|=b
        b1=0
        i=0
        c1=0
        ans=0
        while(i<len(s)):
            if(c1==c2):
                ans+=1
            j=ord(s[i])-97
            b=1<<j
            if(b1&b==0):
                c1+=1
            b1|=b
            if(index[j]<=i):
                b2^=b
                c2-=1
            i+=1
        return ans
                
                