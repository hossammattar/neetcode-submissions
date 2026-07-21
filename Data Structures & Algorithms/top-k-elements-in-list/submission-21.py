class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(counter , key = lambda keys:counter[keys])[len(set(nums))-k:len(set(nums))]
