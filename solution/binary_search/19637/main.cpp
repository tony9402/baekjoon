// Authored by : tallua_y
// Co-authored by : -
// Link : http://boj.kr/8685d839f8704dc697d2d62a8a4c6925

#include <bits/stdc++.h>

using namespace std;

size_t find_ge(const vector<int>& power_levels, const int power, size_t l, size_t r)
{
    if (r <= l + 1) {
        if (power_levels[l] < power) {
            return l + 1;
        }

        return l;
    }

    const size_t mid = (l + r) / 2u;
    if (power < power_levels[mid]) {
        return find_ge(power_levels, power, l, mid);
    } else {
        return find_ge(power_levels, power, mid, r);
    }
}

size_t lower_bound(const vector<int>& power_levels, const int power)
{
    return find_ge(power_levels, power, 0u, power_levels.size());
}

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    size_t N, M;
    cin >> N >> M;

    vector<int> title_levels;
    vector<string> title_names;

    title_levels.reserve(N);
    title_names.reserve(N);

    while (N--)
    {
        int level;
        string name;
        cin >> name >> level;

        if (!title_levels.empty() && title_levels.back() == level) {
            continue;
        }

        title_levels.push_back(level);
        title_names.push_back(name);
    }

    while (M--)
    {
        int power_level;
        cin >> power_level;

        const auto index = lower_bound(title_levels, power_level);

        cout << title_names[index] << '\n';
    }

    return 0;
}