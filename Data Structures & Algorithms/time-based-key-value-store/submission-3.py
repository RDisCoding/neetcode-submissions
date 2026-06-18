class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append({timestamp: value})
        print(self.mapping)

    def get(self, key: str, timestamp: int) -> str:
        if not self.mapping.get(key, 0): return ""

        array = [list(inner_dict.keys())[0] for inner_dict in self.mapping[key]]
        print(array)
        l = 0
        r = len(array) - 1
        res = l
        idx = 0
        print(l)
        print(r)
        print(res)
        while l<=r:
            mid = (l+r)//2
            if array[mid] == timestamp:
                return self.mapping[key][mid][timestamp]
            elif array[mid] < timestamp:
                idx = mid
                res = array[mid]
                l = mid + 1
            else:
                r = mid - 1
        return self.mapping[key][idx][res] if self.mapping[key][idx].get(res, 0) else ""