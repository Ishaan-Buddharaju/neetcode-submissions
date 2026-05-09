class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // vector<int> clean;
        // for (int element : nums) {
        //     if (element != val) {
        //         clean.push_back(element);
        //     }
        // }

        int i = 0;
        for (int j = 0; j < nums.size(); j ++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;        
    }
};