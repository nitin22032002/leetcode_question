class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d={}
        # ts=0
        for i in range(len(wall)):
            s=0
            for j in range(len(wall[i])-1):
                s+=wall[i][j]
                if(s not in d):
                    d[s]=1
                else:
                    d[s]+=1
        ans=len(wall)
        n=len(wall)
        for item in d:
            # if(d[item])
            ans=min(ans,n-d[item])
        return ans