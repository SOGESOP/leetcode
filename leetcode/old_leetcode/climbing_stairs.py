# n=number of stairs
# treeeees!


class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for i in range(n-1):
            temp=a
            a=a+b
            b=temp
        return a
        # every depth you go down you double in nodes at that depth, then you need to consider the shortest path