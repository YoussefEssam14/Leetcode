#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    int deleteGreatestValue(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        vector<priority_queue<int>> heaps(m); // max_heap by def
        for (int i = 0; i < m; i++)
            for (int val : grid[i])
                heaps[i].push(val);
        
        int result = 0;
        
        for (int col = 0; col < n; col++) {
            int roundMax = 0;
            for (int i = 0; i < m; i++) {
                roundMax = max(roundMax, heaps[i].top());
                heaps[i].pop();
            }
            result += roundMax;
        }
        
        return result;
    }
};