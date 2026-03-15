#include <cmath>
#include <queue>
using namespace std;
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int,vector<int>> pq(gifts.begin(),gifts.end());
        for(int i = 0 ; i < k ;i++){
            int top = pq.top();pq.pop();
            pq.push((int)sqrt(top));
        }
        long long sum = 0;
        while(!pq.empty()){
            sum += pq.top();
            pq.pop();
        }
        return sum;
    }
};