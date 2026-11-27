class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand.sort()
        cnt=collections.Counter(hand)

        minh=list(cnt.keys())
        heapq.heapify(minh)

        while minh:
            first=minh[0]

            for i in range(first,first+groupSize):
                if i not in cnt:
                    return False
                cnt[i]-=1
                if cnt[i]==0:
                    if i!=minh[0]:
                        return False
                    heapq.heappop(minh)
        
        return True
        