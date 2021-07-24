// Authored by : tallua_y
// Co-authored by : tony9402
// Link : http://boj.kr/f9b5128041b54d33822f60534944128c
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> title_levels;
    vector<string> title_names;

    title_levels.reserve(N);
    title_names.reserve(N);

    for(int i = 0; i < N; i++) {
        string name;
        int level;
        cin >> name >> level;

        if (!title_levels.empty() && title_levels.back() == level) {
            continue;
        }

        title_levels.push_back(level);
        title_names.push_back(name);
    }

    for(int i = 0; i < M; i++) {
        int power_level;
        cin >> power_level;

        int index = lower_bound(title_levels.begin(), title_levels.end(), power_level) - title_levels.begin();
        cout << title_names[index] << '\n';
    }

    return 0;
}
