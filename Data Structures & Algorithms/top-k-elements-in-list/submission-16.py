class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        l = sorted(counter , key = lambda keys:counter[keys])
        res = []
        for i in range(k):
            res.append(l[len(l)-1-i])
        return res