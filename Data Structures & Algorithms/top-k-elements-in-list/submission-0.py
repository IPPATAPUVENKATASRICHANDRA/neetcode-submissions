class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        nums.sort()   # sort first

        ans = []

        prev_val = nums[0]
        prev_pnt = 0

        freq_list = []

        for cur_pnt in range(1, len(nums)):

            if prev_val != nums[cur_pnt]:

                prev_len = cur_pnt - prev_pnt

                freq_list.append((prev_val, prev_len))

                prev_pnt = cur_pnt
                prev_val = nums[cur_pnt]

        # last element group
        prev_len = len(nums) - prev_pnt
        freq_list.append((prev_val, prev_len))

        # sort based on frequency
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # take top k frequent elements
        for i in range(k):
            ans.append(freq_list[i][0])

        return ans