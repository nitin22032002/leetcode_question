class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        d=[]
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(s[i]==t[i]):
                continue
            elif(s[i]>t[i]):
                cost=(ord("z")-ord(s[i]))+(ord(t[i])-ord("a"))+1
            else:
                cost=ord(t[i])-ord(s[i])
            d.append(cost)
        d.sort()
        if(len(d)>k):
            return False
        else:
            i=0
            while(i<len(d)):
                j=i
                while(j<len(d) and d[i]==d[j]):
                    j+=1
                cycle=(j-i-1)
                if(k<(26*cycle)+d[i]):
                    return False
                i=j
            return True