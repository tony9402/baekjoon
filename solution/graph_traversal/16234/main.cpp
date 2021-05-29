// Authored by : seastar105
// Co-authored by : -
// Link : https://www.acmicpc.net/source/share/628806951c694c76a58fa0c5e510d10f
#include<bits/stdc++.h>

using namespace std;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
int N;
int a[55][55];
bool vis[55][55];
int L, R;

bool valid(int y, int x) {
	return 0 <= y && y < N && 0 <= x && x < N;
}

bool bfs() {
	bool flag = false;
	queue<pair<int,int>> q;
	vector<vector<pair<int,int>>> comp;
	vector<int> comp_pop;
	memset(vis, false, sizeof(vis));
	// bfs
	for(int i=0;i<N;++i) {
		for(int j=0;j<N;++j) {
			if(vis[i][j]) continue;
			vector<pair<int,int>> cur;
			int sum = 0;
			q.emplace(i, j);
			vis[i][j] = true;
			while(!q.empty()) {
				int y = q.front().first;
				int x = q.front().second;
				q.pop();
				sum += a[y][x];
				cur.emplace_back(y, x);
				for(int k=0;k<4;++k) {
					int ny = y + dy[k];
					int nx = x + dx[k];
					int diff = abs(a[y][x] - a[ny][nx]);
					if(!valid(ny, nx) || vis[ny][nx]) continue;
					if(diff > R || diff < L) continue;
					flag = true;
					vis[ny][nx] = true;
					q.emplace(ny, nx);
				}
			}
			comp.push_back(cur);
			comp_pop.push_back(sum);
		}
	}
	if(!flag) return false;
	// population moving
	for(int i=0;i<comp.size();++i) {
		int pop = comp_pop[i] / comp[i].size();
		for(pair<int, int> p : comp[i]) a[p.first][p.second] = pop;
	}
	return true;
}

int main() {
	cin.tie(nullptr); ios::sync_with_stdio(false);
	cin >> N >> L >> R;
	for(int i=0;i<N;++i) {
		for(int j=0;j<N;++j) {
			cin >> a[i][j];
		}
	}
	int ans = 0;
	while(bfs()) ++ans;
	cout << ans << '\n';
	return 0;
}
