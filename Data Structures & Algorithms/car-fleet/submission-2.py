class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = (target - position[i])/speed[i]
        cars = sorted(cars.items())

        stack = []
        cnt = 0
        for x in cars:
            while stack and x[1] >= stack[-1][1]:
                stack.pop()
                cnt-=1
            stack.append(x)
            cnt+=1
        return cnt