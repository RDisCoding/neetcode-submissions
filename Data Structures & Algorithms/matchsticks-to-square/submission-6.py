class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        goal =  sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0,0,0,0]

        def dfs(i):
            if i == len(matchsticks): 
                return True
            
            for s in range(len(sides)):
                if sides[s] + matchsticks[i] <= goal:
                    sides[s] += matchsticks[i]
                    if dfs(i+1): 
                        return True
                    sides[s] -= matchsticks[i]
            return False

        return dfs(0)
        


            