class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1=set(nums1)
        d2=set(nums2)
        return list(d1.intersection(d2))