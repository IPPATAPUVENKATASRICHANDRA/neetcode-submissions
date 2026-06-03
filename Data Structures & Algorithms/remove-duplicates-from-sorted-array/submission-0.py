class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unq=sorted(set(nums))

        nums[:len(unq)]=unq

        return len(unq)
