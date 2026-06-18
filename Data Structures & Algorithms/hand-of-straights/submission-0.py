class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: 
            return False

        hand.sort()
        f = Counter(hand)

        for h in hand:
            if f[h]:
                for i in range(h, h+groupSize):
                    if not f[i]: return False
                    f[i] -= 1

        return True