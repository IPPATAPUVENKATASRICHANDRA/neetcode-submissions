class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if self.checker(weights, mid, days):
                high = mid - 1
            else:
                low = mid + 1

        return low


    def checker(self,weights,target,goal):
        days_used = 1
        curr = 0

        for w in weights:
            if curr + w > target:
                days_used += 1
                curr = w
            else:
                curr += w

        return days_used <= goal
            

