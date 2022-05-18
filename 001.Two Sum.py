class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i,num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num],i]
            else:
                dic[num] = i

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))