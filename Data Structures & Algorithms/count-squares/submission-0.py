class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []


    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        self.pts_count[pt] += 1
        self.pts.append(pt)


    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point

        for x,y in self.pts:
            if abs(qx - x) != abs(qy - y) or qx == x or qy == y:
                continue
            
            pt1 = (qx, y)
            pt2 = (x, qy)

            res += self.pts_count[pt1]*self.pts_count[pt2]
        return res
