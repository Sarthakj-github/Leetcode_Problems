class Solution {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1, m;

        // Edge case: if the array has only one element
        if (j == 0) {
            return nums[0] == target ? 0 : -1;
        }

        while (i <= j) {
            m = (i + j) / 2;
            if (nums[m] == target) return m;

            // Determine which side is sorted
            if (nums[i] <= nums[m]) { // Left side is sorted
                if (nums[i] <= target && target < nums[m]) {
                    j = m - 1; // Target is in the left sorted part
                } else {
                    i = m + 1; // Target is in the right part
                }
            } else { // Right side is sorted
                if (nums[m] < target && target <= nums[j]) {
                    i = m + 1; // Target is in the right sorted part
                } else {
                    j = m - 1; // Target is in the left part
                }
            }
        }
        return -1; // Target not found
    }
}
