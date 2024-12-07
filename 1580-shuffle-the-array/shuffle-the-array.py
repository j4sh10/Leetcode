class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        group1 = nums[:n]
        group2 = nums[n:]
        new_list = []
        for i in range(n):
            new_list.append(group1[i])
            new_list.append(group2[i])
        return new_list
        