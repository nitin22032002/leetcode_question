class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def key(val):
            return [abs(val-x),val]
        arr.sort(key=key)
        arr=arr[:k]
        arr.sort()
        return arr