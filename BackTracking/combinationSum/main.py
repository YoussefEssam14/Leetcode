class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        solution = []
        def backtrack(target,cur,start):
            if target == 0:
                solution.append(cur)
                return
            for i in range(start,len(candidates)):
                if target - candidates[i] >= 0:
                    backtrack(target-candidates[i],cur + [candidates[i]],i)

        backtrack(target,[],0)
        return solution
