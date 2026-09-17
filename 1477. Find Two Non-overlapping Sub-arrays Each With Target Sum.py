class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_combined_len = float('inf')
        best_len_so_far = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == target:
                length = right - left + 1
                
                if left > 0 and best[left - 1] != float('inf'):
                    min_combined_len = min(min_combined_len, length + best[left - 1])
                
                best_len_so_far = min(best_len_so_far, length)
            
            best[right] = best_len_so_far
            
        return min_combined_len if min_combined_len != float('inf') else -1
