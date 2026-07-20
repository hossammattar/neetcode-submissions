class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def siftdown(i:int,n:int)->list[int]:
            if i > n//2-1:
                return nums
            largest = i
            if (i*2+1 <= n-1)and (nums[i] < nums[i*2+1]):
                largest = i*2+1
            if (i*2+2 <= n-1) and (nums[largest] < nums[i*2+2]):
                largest = i*2+2
            temp = nums[largest]
            if largest != i:    
                nums[largest] = nums[i]
                nums[i] = temp
                siftdown(largest,n)


        def heapify()->list[int]:
            for i in range(len(nums)//2 -1,-1,-1):
                siftdown(i,len(nums))
        
        heapify()
        
        i = len(nums)-1
        while i >= 0:
            temp = nums[i]
            nums[i] = nums[0]
            nums[0] = temp
            i -= 1
            siftdown(0,i+1)
        

            