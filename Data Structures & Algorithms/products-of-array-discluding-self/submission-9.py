class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num:
                product *= num
            else: 
                zero_count += 1
        res = []
        for num in nums:
            if(zero_count == 0):
                res.append(product//num)
            elif not num and (zero_count == 1):
                res.append(product)
            elif zero_count !=0:
                res.append(0)
          
        return res