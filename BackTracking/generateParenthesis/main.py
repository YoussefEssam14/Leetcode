class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        sol = []
        def backtrack(open,close,cur):
            # target achieved
            if open + close == 2*  n:
                sol.append(cur)
            # taking two decisions based on constraints
            if open < n:
                # make choice and undo it
                backtrack(open+1,close,cur+"(")
            if close < open:
                # make choice and undo it
                backtrack(open,close+1,cur+")")
        backtrack(0,0,"")
        return sol