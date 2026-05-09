class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        // brute force O(n) time and space
        // copy twice

        vector<int> ans = nums;
        for (int i = 0; i < nums.size(); i++) {
            ans.push_back(nums[i]);
        }

        return ans;
    }
};