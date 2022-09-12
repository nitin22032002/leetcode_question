class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans=0
        i=0
        score=0
        j=len(tokens)-1
        while(j>=i):
            if(tokens[i]<=power):
                power-=tokens[i]
                i+=1
                score+=1
            else:
                if(score>=1):
                    power+=tokens[j]
                    j-=1
                    score-=1
                else:
                    break
            ans=max(ans,score)
        return ans