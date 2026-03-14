#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int subarraySum(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        std::vector<int> prefixSum(n);
        std::partial_sum(nums.begin(), nums.end(), prefixSum.begin());

        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            int start = std::max(0, i - nums[i]);
            
            if (start > 0) {
                totalSum += (prefixSum[i] - prefixSum[start - 1]);
            } else {
                totalSum += prefixSum[i];
            }
        }
        return totalSum;
    }
};