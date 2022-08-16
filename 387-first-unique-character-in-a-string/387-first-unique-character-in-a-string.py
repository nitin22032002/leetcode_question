class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=[0 for _ in range(26)]
        for item in s:
            j=ord(item)-97
            d[j]+=1
        for i in range(len(s)):
            if(d[ord(s[i])-97]==1):
                return i
        return -1