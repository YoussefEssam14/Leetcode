class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        priority_queue<int,vector<int>,greater<int>> pq(nums.begin(),nums.end());
        vector<int> result;
        while(pq.size() != 0){
            int alice = pq.top(); pq.pop();
            int bob = pq.top(); pq.pop();
            result.push_back(bob);
            result.push_back(alice);
        }
        return result;
    }
};