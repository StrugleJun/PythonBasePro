"""
1. 两数之和
https://leetcode.cn/problems/two-sum/description/

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

"""

import cProfile
from typing import List


class Solution:

    def two_sum01(self, nums: List[int], target: int) -> List[int]:
        """
        思路·1 —— 暴力搜索
        使用双重for循环，外层是当前数，内层寻找匹配数，判断两数之和是否为target
        时间复杂度 O(n^2)
        空间复杂度 O(1)


        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum02(self, nums, target):
        """
        思路·2 —— 双指针
        1、首先需要对原数组进行排序，但需要保留原始的下标，因此使用元组排序，会默认先对（num，i）中的num从小到大排序，并且保留了对应的下标i
        2、然后双指针对撞，
              如果两数之和小了，就自增i；
              两数之和大了，就自增j；
              直到两数之和等于target

        双指针只需要遍历一次数组，但内置排序是耗时最大的

        :param nums:
        :param target:
        :return:
        """

        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                nums = sorted((num, i) for i, num in enumerate(nums))
                l, r = 0, len(nums) - 1
                while l < r:
                    cur_sum = nums[l][0] + nums[r][0]
                    if cur_sum == target:
                        return [nums[l][1], nums[r][1]]
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1

    def two_sum03(self, nums: List[int], target: int) -> List[int]:
        """
        思路·3 —— 哈希查找
        为了减小时间复杂度，我们常常会用空间换时间的思路，而利用哈希表查找O（1）的特性，通常可以增加额外的哈希表来加快搜索速度！
        1、首先明确此题哈希的用法，我们是需要找到和为target的两个数的下标，因此map的key为数字，value为下标
        2、循环遍历一次数组
             2.1 查找互补数sup（即target-num）是否在map中
             2.2 若在直接返回
             2.3 将num和i作为键值对加入到map中
        时间复杂度: O(n)
        空间复杂度: O(n)
        :param nums:
        :param target:
        :return:
        """
        nums_map = dict()
        for index, num in enumerate(nums):
            sup = target - num
            if sup in nums_map:
                return [nums_map[sup], index]
            else:
                nums_map[num] = index


if __name__ == '__main__':
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    cProfile.run('solution.two_sum03(nums, target)')
