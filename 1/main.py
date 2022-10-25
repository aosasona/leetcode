class Solution:
    def twoSum(self, nums, target: int):
        prev = 0
        final = [0, 0]
        for i, v in enumerate(nums):
            if i == prev:
                continue
            else:
                prev = i
                for k, n in enumerate(nums):
                    if k != i:
                        val = v + n
                        if val == target:
                            final = [i, k]
                            break
        return final


sol = Solution()
res = sol.twoSum([1, 2, 3, 4, 5], 4)
print(res)
