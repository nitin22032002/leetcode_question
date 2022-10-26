class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mid=(len(arr)-1)//2
        m=arr[mid]
        def key(val):
            return [abs(val-m),val]
        arr.sort(key=key,reverse=True)
        return arr[:k]