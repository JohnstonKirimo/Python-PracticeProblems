"""

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

"""
#sample solution
class Solution:
    def divide(self, devident: int, devisor: int) -> int:
        positive = ((devident>0) and (devisor>0)) or ((devident<0) and (devisor<0))
        devident, devisor = abs(devident), abs(devisor)
        current_val, coef, answer = devisor, 1, 0
        while(devisor<=devident):
            # binary devision
            if current_val+current_val<=devident:
                current_val += current_val
                coef += coef
            else:
                answer += coef
                devident -= current_val
                current_val, coef = devisor, 1
        if (positive) and (answer == 2**31):
            return 2**31-1
        return answer if positive else -answer
