class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        i=0
        j=0
        ans=0
        count=0
        while(j<len(fruits)):
            if(count<=2):
                ans=max(ans,(j-i))
                if(fruits[j] in d):
                    d[fruits[j]]+=1
                else:
                    d[fruits[j]]=1
                    count+=1
                j+=1
            else:
                d[fruits[i]]-=1
                if(d[fruits[i]]==0):
                    del d[fruits[i]]
                    count-=1
                i+=1
        while(i<len(fruits)):
            if(count<=2):
                ans=max(ans,(j-i))
                break
            else:
                d[fruits[i]]-=1
                if(d[fruits[i]]==0):
                    del d[fruits[i]]
                    count-=1
                i+=1
        
        return ans
                