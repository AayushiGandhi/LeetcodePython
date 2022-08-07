#https://leetcode.com/problems/slowest-key/submissions/
#https://www.youtube.com/watch?v=8of27byorT8&ab_channel=SaiAnishMalla

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = releaseTimes[0]
        result = keysPressed[0]

        for index in range(1, len(keysPressed)):
            current_time = releaseTimes[index] - releaseTimes[index - 1]
            if current_time > time:
                time = current_time
                result = keysPressed[index]
            elif current_time == time:
                result = max(keysPressed[index], result)

        return result
