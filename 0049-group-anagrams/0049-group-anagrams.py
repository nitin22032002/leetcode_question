class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for item in strs:
            item1=self.sorted(item)
            if(item1 in d):
                d[item1].append(item)
            else:
                d[item1]=[item]
        return list(d.values())
    def sorted(self,s):
        d=[0 for _ in range(26)]
        for item in s:
            d[ord(item)-97]+=1
        ans=[]
        for i in range(26):
            if(d[i]!=0):
                ans.append(chr(i+97)*d[i])
        return "".join(ans)