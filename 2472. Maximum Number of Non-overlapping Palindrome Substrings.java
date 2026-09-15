class Solution {
    public int maxPalindromes(String s,int k){
        int res=0,n=s.length();
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                int len=j-i+1;
                if(len>k+1)break;
                if(len>=k&&isPal(s,i,j)){
                    res++;
                    i=j;
                    break;
                }
            }
        }
        return res;
    }

    private boolean isPal(String s,int l,int r){
        while(l<r){
            if(s.charAt(l++)!=s.charAt(r--))return false;
        }
        return true;
    }
}
