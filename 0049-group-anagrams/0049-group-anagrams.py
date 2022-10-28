class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for item in strs:
            item1="".join(sorted(item))
            if(item1 in d):
                d[item1].append(item)
            else:
                d[item1]=[item]
        return list(d.values())