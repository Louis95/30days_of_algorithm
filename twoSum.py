class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lists = []
        # for y in range(len(nums)):
        #     for x in range(y+1, len(nums)):
        #         if (nums[x] == target - nums[y]):
        #             lists.extend((x, y))
        # return lists
        
        #solving using
        dic_map = {}
        for x, y in enumerate(nums):
            m = target - y
            if m in dic_map:
                return [dic_map[m], x]
            else:
                dic_map[y] = x