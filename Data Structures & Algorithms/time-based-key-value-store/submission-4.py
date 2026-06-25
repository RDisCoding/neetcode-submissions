class TimeMap:

    def __init__(self):
        self.tm = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm: return ""
        search = self.tm[key]
        search = sorted(search.items())
        print(search)
        i = 0
        j = len(search)-1
        while i<=j:
            mid = i+(j-i)//2
            if search[mid][0] == timestamp:
                return search[mid][1]
            elif search[mid][0] < timestamp:
                i = mid + 1
            else:
                j = mid - 1
        return search[j][1] if search[j][0] <= timestamp else ""