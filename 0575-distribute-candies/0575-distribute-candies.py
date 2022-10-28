class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        m=len(set(candyType))
        return min(m,n//2)