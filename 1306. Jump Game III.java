class Solution {
    public boolean canReach(int[] arr, int start) {
        if(arr[start]==0)
            return true;
        int n = arr.length;
        Queue<Integer> Q = new LinkedList();
        Set<Integer> S = new HashSet();
        Q.add(start);
        S.add(start);

        while(!Q.isEmpty()){
            int q = Q.poll();
            int pq=q-arr[q],fq=q+arr[q];
            if(pq>=0 && !S.contains(pq)){
                if(arr[pq]==0)  return true;
                else{
                    Q.add(pq);
                    S.add(pq);
                }
            } 
            if(fq<n && !S.contains(fq)){
                if(arr[fq]==0)  return true;
                else{
                    Q.add(fq);
                    S.add(fq);
                }
            }
        }
        return false;
    }
}
