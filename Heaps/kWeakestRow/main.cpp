#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        // Max-heap {soldierCount,rowIndex}
        auto cmp = [](pair<int,int>& a,pair<int,int>& b){
            return a.first != b.first ? a.first < b.first : a.second < b.second;
        };
        priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(cmp)> maxHeap(cmp);
        for(int i =0 ; i < mat.size() ;i++){
            int count = countSoldiers(mat[i]);
            maxHeap.push({count,i});
            if(maxHeap.size() > k){
                maxHeap.pop();
            }
        }
        vector<int> result(k);
        for(int i = k-1 ;i >=0 ;i--){
            result[i] = maxHeap.top().second; maxHeap.pop();

        }
        return result;
    }

private:
    int countSoldiers(vector<int>& row) {
        int lo = 0, hi = row.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (row[mid] == 1) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
};
