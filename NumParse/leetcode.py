#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path as op
import sys


class ListNode(object):
    "Definition for link list.(1 -> 2 -> 3)."

    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def searchInsert(self, nums, target):
        """
        This is mine first solution for this problem.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        try:
            return nums.index(target)
        except ValueError:
            max_index = len(nums) - 1
            if nums[0] < target < nums[max_index]:
                for i in range(1, max_index + 1):
                    left = i - 1 if i > 0 else 0
                    right = i if i < max_index else max_index

                    if nums[left] < target < nums[right]:
                        return i
            elif nums[0] > target:
                return 0
            elif nums[max_index]:
                return max_index + 1

    def searchInsert2(self, nums, target):
        """
        This solution is copy from leetcode user xiaoying10101.
         https://leetcode.com/problems/search-insert-position/discuss/15427/Accepted-O(logN)-solution-Python
        :param nums: list
        :param target: int
        :return: int.
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if mid == 0:
                    return mid
                elif nums[mid - 1] < target:
                    return mid
                else:
                    end = mid - 1
                    continue
            elif nums[mid] < target:
                start = mid + 1
                continue
        return end +1

    def myPow(self, x, n):
        """
        Leetcode problem myPow.
        :param x: float
        :param n: int
        :return: float
        """

        print('haonan')