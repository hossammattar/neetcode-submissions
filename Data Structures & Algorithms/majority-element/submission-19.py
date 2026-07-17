class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return sorted(Counter(nums).items(), key=lambda item: item[1])[-1][0]
        