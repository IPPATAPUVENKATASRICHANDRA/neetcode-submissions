class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1

        while i<=len(numbers)-1 and j>=0:
            val=numbers[i]+numbers[j]
            if val == target:
                return [i+1,j+1]
            
            elif target<=val:
                j=j-1
            else:
                i=i+1
        
        return []