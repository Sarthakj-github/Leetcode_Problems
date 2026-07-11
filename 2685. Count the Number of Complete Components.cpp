class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        
        vector<vector<int>> graph(n);
        for(int i=0;i<edges.size();i++){
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }

        vector<bool> vis(n,false);
        int c=0;
        for(int i=0;i<n;i++){
            if(!vis[i]){
                vector<int> component;
                dfs(i,graph,vis,component);
                int k=component.size();
                bool f=true;
                for(int j:component){
                    if(graph[j].size()!=(k-1)){
                        f=false;    break;
                    }
                }
                if(f)   c++;
            }
        }
        return c;
    }
    void dfs(int i,vector<vector<int>>& graph,vector<bool>& vis,vector<int>& component){
        vis[i]=true;
        component.push_back(i);
        for(int j:graph[i]){
            if(!vis[j]) dfs(j,graph,vis,component);
        }
    }
};
