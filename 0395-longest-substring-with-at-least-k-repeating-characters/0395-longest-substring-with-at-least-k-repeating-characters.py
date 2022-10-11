class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique=0
        bit=0
        for item in s:
            j=ord(item)-97
            b=1<<j
            if(bit&b==0):
                maxUnique+=1
            bit|=b
        ans=0
        for curr in range(1,maxUnique+1):
            i=0
            j=0
            d={}
            count=0
            while(j<len(s)):
                if(curr==len(d) and curr==count):
                    ans=max(ans,j-i)
                if(len(d)<=curr):
                    if(s[j] in d):
                        d[s[j]]+=1
                    else:
                        d[s[j]]=1
                    if(d[s[j]]==k):
                        count+=1
                    j+=1
                elif(len(d)>curr):
                    if(d[s[i]]==k):
                        count-=1
                    d[s[i]]-=1
                    if(d[s[i]]==0):
                        del d[s[i]]
                    i+=1
            while(i<len(s) and len(d)>curr):
                if(d[s[i]]==k):
                    count-=1
                d[s[i]]-=1
                if(d[s[i]]==0):
                    del d[s[i]]
                i+=1
            if(count==curr):
                ans=max(ans,j-i)
        return ans
                    