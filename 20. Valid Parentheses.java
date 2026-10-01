class Solution {
    Map<Character,Character> d = new HashMap();
    public boolean isValid(String s) {
        d.put(')','(');
        d.put('}','{');
        d.put(']','[');
        Stack<Character> S = new Stack<>();
        char p;
        for(int i=0;i<s.length();i++){
            p=s.charAt(i);
            if(d.containsKey(p)){
                if(S.isEmpty() || S.peek()!=d.get(p))   return false;
                else    S.pop();
            }
            else    S.push(p);
        }
        return S.isEmpty();
    }
}
