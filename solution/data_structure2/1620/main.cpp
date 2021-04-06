#include<bits/stdc++.h>

using namespace std;

// map으로 해도 상관없지만, 순서에는 상관이 없으니 unordered_map으로 사용
unordered_map<string, string> pokemon;
unordered_map<string, string> pokemonSeq;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q; cin >> N >> Q;
    for(int i=1;i<=N;i++){
        string s; cin >> s;
        string idx = to_string(i);
        pokemon[s]      = idx;
        pokemonSeq[idx] = s;
    }
    
    while(Q--) {
        string s; cin >> s;
        if(isdigit(s[0])) {
            cout << pokemonSeq[s] << '\n';
        }
        else {
            cout << pokemon[s] << '\n';
        }
    }

    return 0;
}
