// Authored by : xhdxhl
// Co-authored by : -
// Link : http://boj.kr/d4f08f292aed46729e98bea45c026da6

#include <bits/stdc++.h>
using namespace std;
 
int n, m, k, parent[51];

vector<int> know;
vector <vector<int>> v(51);
 
int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}
 
void merge(int x, int y) {
    x = find(x);
    y = find(y);
    parent[x] = y;
}

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m >> k;
 
    while (k--) {
        int t;
        cin >> t;
        know.push_back(t);
    }
 
    for (int i = 1; i <= n; i++) parent[i] = i;
 
    for (int i = 0; i < m; i++) {
        int p, num, prev;
        cin >> p;
        for (int j = 0; j < p; j++) {
            if (j >= 1) {
                prev = num;
                cin >> num;
                merge(prev, num);
            }
            else cin >> num;
            v[i].push_back(num);
        }
    }

    for (auto& list : v) {
        bool flag = false;
        for (auto& person : list) {
            for (auto& t : know) {
                if (find(person) == find(t)) {
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        if(flag) m--;
    }
    cout << m;
}
