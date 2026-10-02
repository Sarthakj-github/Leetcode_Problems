class Solution {
    List<String> ans;
    public List<String> generateParenthesis(int n) {
        ans = new ArrayList<>();
        solve(n,"",0);
        return ans;
    }
    void solve(int n,String s,int p){
        if(n==0 && p==0)    ans.add(s);
        if(n!=0)
            solve(n-1,s+"(",p+1);
        if(p!=0)
            solve(n,s+")",p-1);
    }
}
