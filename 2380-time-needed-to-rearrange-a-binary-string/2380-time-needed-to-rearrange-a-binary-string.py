class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans=0
        s=list(s)
        c=s.count("1")
        i=0
        ans=0
        while(True):
            # print(s)
            while(i<len(s) and s[i]=="1"):
                i+=1
            j=i+1
            if(i==c):
                break
            t=i
            while(j<len(s)):
                if(s[i]=="0" and s[j]=="1"):
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j+=1
                i+=1
                j+=1
            i=t
            ans+=1
        return ans
                
            