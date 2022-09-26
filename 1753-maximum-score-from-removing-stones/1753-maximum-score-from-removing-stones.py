class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles=[a,b,c]
        piles.sort()
        score=0
        while(piles[-2]!=0):
            score+=1
            piles[-1]-=1
            piles[-2]-=1
            piles.sort()
        return score