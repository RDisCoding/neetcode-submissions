class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            j = i
            tank = 0
            while True:
                tank += gas[j] - cost[j]
                if tank < 0: 
                    break
                j = (j+1)%len(gas)
                if j == i:
                    print(i)
                    return i
        return -1
