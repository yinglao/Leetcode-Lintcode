# 难点在于去重：既要保证能够选到相同的元素，又要保证不会出现重复的组合。
# 策略是，保证每次选一系列相同的数时，只选第一个遇到的作为开头
# 14 - 21， 26 - 31

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        prei = None
        for i in range(len(nums)):
            if nums[i] == prei:
                continue
            prej = None
            for j in range(i + 1, len(nums)):
                if nums[j] == prej:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
                
                prej = nums[j]
            prei = nums[i]
        return res
