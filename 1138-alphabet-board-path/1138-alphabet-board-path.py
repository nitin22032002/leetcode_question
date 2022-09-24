class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans=[]
        curr=[0,0]
        for item in target:
            path=self.findPath(ord(item)-97,curr)
            ans.append(path)
        return "".join(ans)
    
    def findPath(self,letter,curr):
        row=(letter//5)
        col=(letter%5)
        r=(row-curr[0])
        c=(col-curr[1])
        ans=""
        if(r<0):
            ans+=(abs(r)*"U")
        else:
            if(letter==25):
                ans+=((r-1)*"D")
            else:
                ans+=(r*"D")
        if(c<0):
            ans+=(abs(c)*"L")
        else:
            ans+=(c*"R")
        curr[0]=row
        curr[1]=col
        if(letter==25 and r!=0):
            ans+="D"
        return ans+"!"
    
        