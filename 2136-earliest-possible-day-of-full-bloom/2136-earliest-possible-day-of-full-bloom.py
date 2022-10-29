class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr=list(zip(plantTime,growTime))
        def key(val):
            return [-val[1],val[0]]
        arr.sort(key=key)
        start=0
        curr=0
        for item in arr:
            start+=item[0]
            curr=max(start+item[1],curr)
        return curr