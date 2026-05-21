class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        Set<Integer> S = new HashSet();
        int ans=0;
        for(int a:arr1){
            while(a!=0){
                S.add(a);
                a/=10;
            }
        }
        for(int b:arr2){
            while(b!=0){
                if(S.contains(b))
                    ans = Math.max(ans,Integer.toString(b).length());
                b/=10;
            }
        }
        return ans;
    }
}
