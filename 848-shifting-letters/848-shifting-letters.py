class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p=sum(shifts)
        ans=list(s)
        for i in range(len(s)):
            j=ord(ans[i])-96
            j+=p
            j%=26
            if(j==0):
                j=26
            ans[i]=chr(96+j)
            p-=shifts[i]
        return "".join(ans)
        