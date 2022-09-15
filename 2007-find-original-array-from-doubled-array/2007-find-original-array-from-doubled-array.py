class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        d={}
        for item in changed:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        changed.sort()
        ans=[]
        i=0
        for item in sorted(d):
            # item=changed[i]
            if(d.get(item,0)>0):
                # print(d.get(2*item,0),d[item])
                if(d.get(2*item,0)>=d[item]):
                    if((2*item)==item):
                        if(d[item]%2!=0):
                            return []
                        else:
                            ans.extend([item]*(d[item]//2))
                        d[item]=0
                    else:
                        d[2*item]-=d[item]
                        ans.extend([item]*d[item])
                else:
                    return []
        return ans
                