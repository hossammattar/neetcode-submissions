class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_items = sorted(counter.items(), key=lambda item: item[1])
        return sorted_items[-1][0]