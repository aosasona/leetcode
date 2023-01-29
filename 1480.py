class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        s = 0
        for idx in range(len(nums)):
            sub_array = nums[0:idx+1]
            print(sub_array)
            s = sum(sub_array)
            result.append(s)
        return result

solution = Solution()
res = solution.runningSum([1,1,1,1])
print(res)
