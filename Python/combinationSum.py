"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

"""
#sample solution (using backtracking)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:                
        def backtrack(curr_comb, target, res, start):
            # check if goal was reached
            if target == 0:
                res.append(curr_comb[:])
            
            # explore our search space
            for idx in range(start, len(candidates)):
                curr_candidate = candidates[idx]
                
                # check if constraints are met (maybe selecting only elements that are greater or equal to last selection)                                
                # if not curr_comb or (candidate >= curr_comb[-1] and candidate <= target):
                if curr_candidate <= target:                
                    # make a choice
                    curr_comb.append(curr_candidate)
                
                    # continue exploration
                    backtrack(curr_comb, target - curr_candidate, res, idx)
                
                    # undo choice
                    curr_comb.pop()
                
        res = []
        backtrack([], target, res, 0)
        
        return res