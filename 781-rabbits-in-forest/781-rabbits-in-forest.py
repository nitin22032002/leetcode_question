from math import ceil
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        for item in answers:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        ans=0
        for item in d:
            ans+=(ceil(d[item]/(item+1))*(item+1))
        return ans
            