class Solution:
    def twoEggDrop(self, n: int) -> int:
        x=pow((1+(8*n)),0.5)
        ans=(-1+x)/2
        if(int(ans)!=ans):
            ans+=1
        return int(ans)