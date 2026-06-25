class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if not change[5]: return False
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                if not change[5]: 
                    return False

                if not change[10]:
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
                else:
                    change[10] -= 1
                    change[5] -= 1
        return True
                

        