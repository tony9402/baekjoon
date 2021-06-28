// Authored by : rlawngus0910
// Co-authored by : -
// Link : http://boj.kr/62feef4ccd1a4b1291e0eb1850a9ad4b

#include <bits/stdc++.h>
using namespace std;
string s, k;
int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cin >> s >> k;

	for (int i = 0; i < s.length(); i++) {
		if (s[i] < '0' || s[i] > '9') continue;
		s.erase(i, 1);
		i--;
	}

	if (s.find(k) != string::npos) cout << "1";
	else cout << "0";
}