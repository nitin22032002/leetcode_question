class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        i=0
        pair=[0,0]
        while(i<len(s1)):
            if(s1[i]!=s2[i]):
                if(s1[i]=="x" and s2[i]=="y"):
                    pair[0]+=1
                else:
                    pair[1]+=1
            i+=1
        s=sum(pair)
        if(s%2!=0):return -1
        else:
            count=(pair[0]//2)+(pair[1]//2)
            left=(pair[0]%2)+(pair[1]%2)
            return count+left
            