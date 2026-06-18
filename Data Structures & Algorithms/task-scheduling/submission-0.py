class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxf = max(c.values())

        n_max_freq_tasks = list(c.values()).count(maxf)

        skeleton = (maxf-1)*(n+1) + n_max_freq_tasks

        return max(skeleton, len(tasks))