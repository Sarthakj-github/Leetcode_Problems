class Solution {
    public int numDistinct(String s, String t) {
        int n = s.length();
        int m = t.length();
        
        int[][] dp = new int[2][m + 1];
        
        dp[0][m] = 1;
        dp[1][m] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (s.charAt(i) == t.charAt(j)) {
                    dp[i % 2][j] = dp[(i + 1) % 2][j + 1] + dp[(i + 1) % 2][j];
                } else {
                    dp[i % 2][j] = dp[(i + 1) % 2][j];
                }
            }
        }

        return dp[0][0];
    }
}
