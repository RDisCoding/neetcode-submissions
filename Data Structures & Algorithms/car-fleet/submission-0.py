class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for p,s in zip(position, speed):
            d = target - p
            times.append((d/s, p))
        
        times.sort(key = lambda x: x[1])

        stack = []
        
        for t in times:
            while stack and t[0] >= stack[-1]:
                stack.pop()
            stack.append(t[0])
        
        return len(stack)