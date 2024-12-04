class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)):
            m = nums[x]
            for i in range(len(nums)):
                n = nums[i]
                if m == n and x < i:
                    # print("match ", x, i)
                    count += 1
        return count
        
        