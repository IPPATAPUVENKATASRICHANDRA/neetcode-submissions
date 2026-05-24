class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()
        new_nums = list(set(nums))
        new_nums.sort()

        print(new_nums)

        st_val = new_nums[0]
        cnt = 1
        maxi = 1

        for i in range(1, len(new_nums)):

            if st_val + 1 == new_nums[i]:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 1

            st_val = new_nums[i]

        maxi = max(maxi, cnt)

        return maxi
