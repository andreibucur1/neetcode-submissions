class Solution:
    def climbStairs(self, n: int) -> int:
        v = [0] * 49
        v[1] = 1
        v[2] = 2
        v[3] = 3
        if n == 1 or n == 2 or n == 3:
            return v[n]
        cnt = 3
        while cnt <= n:
            cnt += 1
            v[cnt] = v[cnt - 1] + v[cnt - 2]

        return v[n]