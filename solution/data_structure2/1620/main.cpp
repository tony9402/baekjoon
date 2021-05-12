// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9289c0621c6f41dabd5bfc2ba190a2ce
#include<bits/stdc++.h>

using namespace std;

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
