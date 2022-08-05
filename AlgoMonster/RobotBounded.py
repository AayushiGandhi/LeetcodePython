class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0

        for i in instructions:
            if i == "G":
                x, y = x + dirX, y + dirY
            elif i == "L":
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX

        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)

#https://www.youtube.com/watch?v=nKv2LnC_g6E&ab_channel=NeetCode
#https://leetcode.com/problems/robot-bounded-in-circle/