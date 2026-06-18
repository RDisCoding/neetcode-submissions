class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = 0
            cnt = 0
            j = i
            tank = gas[i]

            while tank - cost[j] >= 0:
                print(j)
                print(tank - cost[j])
                tank -= cost[j]
                j = (j+1)%n
                tank += gas[j]
                cnt +=1
                if cnt == n: 
                    return i

        return -1
