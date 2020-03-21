# 访问所有点的最短路程

from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for index,item in enumerate(points):
            if index == len(points)-1:
                return total
            total+=max(abs(item[0]-points[index+1][0]), abs(item[1]-points[index+1][1]))
        return total

if __name__ == '__main__':
    solution = Solution()
    print(solution.minTimeToVisitAllPoints([[3,2],[-2,2]]))
    # print(len([1,2,3])-1)
    