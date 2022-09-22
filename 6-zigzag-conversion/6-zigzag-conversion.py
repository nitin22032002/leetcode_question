class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows<2):
            return s
        ans=[]
        for i in range(numRows):
            k=i
            gap=1
            bit=True
            while(k<len(s)):
                if(gap!=0):
                    ans.append(s[k])
                if(bit):
                    gap=2*(numRows-i-1)
                else:
                    gap=2*i   
                k+=gap
                bit=not bit
        return "".join(ans)
                