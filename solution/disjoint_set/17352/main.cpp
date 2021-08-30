// Authored by : bakh1
// Co-authored by : -
// Link : http://boj.kr/a55613bb803d46ce8e3cbc399ac6427d

#include <bits/stdc++.h>
using namespace std;
#define SET_SIZE 300010

struct DisjointSet{
    int parent[SET_SIZE];
    
    int find(int x){
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    void Union(int x, int y){
        x=find(x);  y=find(y);
        if(x!=y) parent[y]=x;
    }
    DisjointSet(){
        for(int i=0; i<SET_SIZE; i++) parent[i]=i;
    }
} st;

int main()
{
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N, a, b, prev;
    cin >> N;
    for(int i=0; i < N-2; i++) {
        cin>>a>>b;
        st.Union(a,b);
    }
    
    prev = st.find(1);
    
    for(int i=1; i<=N; i++){
        if(st.find(i) != prev){
            cout << prev << " " << st.find(i) << "\n";
            break;
        }
        prev = st.find(i);
    }
    
    return 0;
}
