class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans=[]
        s=s.upper()
        i=len(s)-1
        while(i>=0):
            j=i
            t=0
            m=[]
            while(t<k and j>=0):
                if(s[j]=="-"):
                    j-=1
                    continue
                m.append(s[j])
                t+=1
                j-=1
            if(len(m)!=0):
                m.reverse()
                m="".join(m)
                ans.append(m)
            i=j
        # print(ans)
        ans.reverse()
        return "-".join(ans)