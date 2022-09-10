class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        i=0
        n=len(s)
        ans=[]
        while(i<=(n-10)):
            t=s[i:i+10]
            if(t in d):
                if(d[t]):
                    ans.append(t)
                    d[t]=False
            else:
                d[t]=True
            i+=1
        return ans
                