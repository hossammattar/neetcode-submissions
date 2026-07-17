class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = Counter(nums)
        l = counter[val]
        for _ in range(l):
            nums.remove(val)
        return len(nums)