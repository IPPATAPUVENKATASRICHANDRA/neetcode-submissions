class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        prefix=0
        freq=defaultdict(int)
        freq[0]=1
        for i in range(len(nums)):
            prefix+=nums[i]
            cnt+=freq[prefix-k]
            freq[prefix]+=1
        
        return cnt