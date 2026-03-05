class Solution:
    def minOperations(self, s: str) -> int:
        # count mismatches with pattern starting with '0': 010101...
        count = sum(1 for i, c in enumerate(s) if c != str(i % 2))
        # if pattern starts with '0' costs `count`, starting with '1' costs `n - count`
        return min(count, len(s) - count)