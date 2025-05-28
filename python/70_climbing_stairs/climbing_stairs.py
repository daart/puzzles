"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45


"""

# worst solution - recursive O(n**2) time
def recursive(n):
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        
        if (n == 2):
            return 2
        if (n == 1):
            return 1
        
        memo[n] = helper(n - 1) + helper(n - 2)
    return helper(n);

t1 = 5;
t2 = 4;

print(recursive(t1))
print(recursive(t2))

# better solution with memoization. O(n) time, still crappy Space 
def memoized_climb_stairs(self, n):
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)

"""
for optimal solution the idea is to go from bottom to top and use pointers.
We will iterate from 0 to n-1. In order to get to current step assuming current step is k  
we should have passed (k-1) + (k-2) ways. current step on each new step will equal to sum of
current ways plus previous ways. 

Example n = 3:
we start al the calculations from 2nd step ways(2) = (ways(2-1) = 1) + (ways(2 - 2) = 1)
So on ways(3) = ways(3-1 = (ways(2-1) = 1)) + (ways(2 - 2) = 1)) + (ways(3-2) = 1)

[1, 1, 2, 3, 5, 8] => ways to reach step (current is the sum of previous two)
[0, 1, 2, 3, 4, 5] => number of steps or step indexes (basically a range from 0 to n we get from input. And since we know that next possible ways is the sum of current ways + previous, we don't need to get to last step, thus range(n-1))

Complexity Time O(n) Space O(1)
"""
def optimal_solution(n):
    prevSteps = 1
    currentSteps = 1

    for i in range(n - 1):
        temp = currentSteps
        currentSteps += prevSteps
        prevSteps = temp

    return currentSteps