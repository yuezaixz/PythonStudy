# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points : return 0;
        length = len(points)
        if length < 3 : return length;
        maxNum = -1
        for i in xrange(length):
            countDict = {'inf': 0}
            # default 1 , because i need count current point 
            samePointsNum = 1
            currPoint = points[i]
            for j in xrange(length):
                targetPoint = points[j]
                # The same position in list
                if i == j : 
                    continue
                # the slop value is inf
                elif currPoint.x == targetPoint.x and currPoint.y != targetPoint.y:
                    countDict['inf'] += 1
                elif currPoint.x != targetPoint.x:
                    # care about the slop value maybe float
                    slop = 1.0*(currPoint.y - targetPoint.y) / (currPoint.x - targetPoint.x)
                    if slop in countDict:
                        countDict[slop] = countDict[slop] + 1
                    else:
                        countDict[slop] = 1
                else:
                    # the current and target is same point
                    samePointsNum += 1
            maxNum = max(maxNum,(max(countDict.values())+ samePointsNum))
        return maxNum

if __name__ == '__main__':
    points = []
    points.append(Point(84,250))
    points.append(Point(0,0))
    points.append(Point(1,0))
    points.append(Point(0,-70))
    points.append(Point(0,-70))
    points.append(Point(1,-1))
    points.append(Point(21,10))
    points.append(Point(42,90))
    points.append(Point(-42,-230))
    so = Solution()
    print so.maxPoints(points)