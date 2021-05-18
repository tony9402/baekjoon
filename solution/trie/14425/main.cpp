// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/3c2d334828274046abfde50531627f0a
#include<bits/stdc++.h>

using namespace std;

struct Trie {
    struct Node {
        char data;
        bool isEnd;
        int nxt[26];
        int &operator[](int idx) { return nxt[idx]; }
        int operator[](int idx) const { return nxt[idx]; }
        Node() : data(0) { memset(nxt, 0xff, sizeof(int) * 26); }
        Node(char data) : data(data)  { memset(nxt, 0xff, sizeof(int) * 26); }
    };
    vector<Node> tree;

    Trie() { tree.emplace_back(); }

    int getIdx(char x) {
        return x - 'a';
    }

    void update(const string &s) { 
        int cur = 0; // Root of Trie
        for(char i: s) {
            int idx = getIdx(i);
            if(!~tree[cur][idx]) {
                tree[cur][idx] = tree.size();
                tree.emplace_back(i);
            }
            cur = tree[cur][idx];
        }
        tree[cur].isEnd = true;
    }

    bool find(const string &s) {
        int cur = 0;
        for(char i: s) {
            int idx = getIdx(i);
            if(!~tree[cur][idx]) return false;
            cur = tree[cur][idx];
        }
        return tree[cur].isEnd;
    }
} trie;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q; cin >> N >> Q;
    for(int i=0;i<N;i++) {
        string s; cin >> s;
        trie.update(s);
    }
    int answer = 0;
    for(int i=0;i<Q;i++) {
        string s; cin >> s;
        if(trie.find(s)) answer ++;
    }
    cout << answer;

    return 0;
}
