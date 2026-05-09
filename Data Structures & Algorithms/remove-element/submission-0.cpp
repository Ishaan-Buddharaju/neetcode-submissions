class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> clean;
        for (int element : nums) {
            if (element != val) {
                clean.push_back(element);
            }
        }

        int i = 0;
        for (int element : clean) {
            nums[i++] = element;
        }
        return i;        
    }
};