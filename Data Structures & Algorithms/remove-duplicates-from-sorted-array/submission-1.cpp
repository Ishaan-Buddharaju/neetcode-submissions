class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> unique{nums.begin(), nums.end()};
        int i = 0;
        for (int val : unique) {
            nums[i++] = val;
        }
        return i;
    }
};