class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted(counter, key=lambda keys: counter[keys])[-1]
        