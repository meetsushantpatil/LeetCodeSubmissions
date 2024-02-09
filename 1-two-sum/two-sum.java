class Solution {
    public int[] twoSum(int[] nums, int target) {

        int cur_num = 0;
        int len = nums.length;
        int[] result = new int[2];

        for (int i = cur_num; i < len - 1; i++) {
            for (int j = i + 1; j < len ; j++) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }

        return result;
    }
}