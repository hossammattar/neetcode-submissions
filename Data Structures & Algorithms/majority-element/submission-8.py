class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        x = max(counter[x] for x in set(nums))
        for key,value in counter.items():
                if value == x:
                    return key