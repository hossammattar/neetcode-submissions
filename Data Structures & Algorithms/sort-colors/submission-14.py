class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)
        base = 0

        for i in range(len(set(nums))):
            
            for j in range(counter[i]):
                nums[j+base] = i

            base += counter[i]
        
        

            