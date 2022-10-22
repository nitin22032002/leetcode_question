class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1={}
        for item in t:
            if(item in d1):
                d1[item]+=1
            else:
                d1[item]=1
        i=0
        j=0
        charge=0
        d={}
        ans=""
        while(j<=len(s) and i<=len(s)):
            if(charge!=len(t) and j<len(s)):
                if(s[j] in d):
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                if(d[s[j]]<=d1.get(s[j],0)):
                    charge+=1
                j+=1
            elif(charge<len(t) and j>=len(s)):
                break
            else:
                d[s[i]]-=1
                if(s[i] in d1 and d1[s[i]]>d[s[i]]):
                    charge-=1
                i+=1
            if(charge==len(t)):
                if(len(ans)>j-i or ans==""):
                    ans=s[i:j]
            
        return ans