/****************************************************************************************************************************/
/*************************************                 My Template Begin                *************************************/
/*************************************                                                  *************************************/
/*************************************    Template Version : 2.0.0                      *************************************/
/*************************************    Made By          : tony9402(Minsang Kim)      *************************************/
/****************************************************************************************************************************/
#ifndef LOCAL
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#endif

#include<bits/stdc++.h>

using namespace std;

/******** #define BEGIN ********/
#define all(x)          (x).begin(),(x).end()
#define sortall(x)      sort(all(x))
#define reverseall(x)   reverse(all(x))
#define siz(x)          (int)(x).size()
#define rep(i, n)       for(int i=0;i<(n);i++)
#define repi(i, l, r)   for(int i=l;i<=(r);i++)
#define rrep(i, n)      for(int i=(n)-1;i>=0;i--)
#define rrepi(i, r, l)  for(int i=r;i>=l;i--)
#define pb push_back
#define pf push_front
#define eb emplace_back
#define ef emplace_front
#define ppb pop_back
#define ppf pop_front
#define fi first
#define se second
/******** #define END ********/

/******** type define BEGIN ********/
using ull = unsigned long long;
using ll  = long long;
using ld  = long double;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
using pil = pair<int, long long>;
using pli = pair<long long, int>;
using vi  = vector<int>;
using vd  = vector<double>;
using vl  = vector<ll>;
using vii = vector<pii>;
using vll = vector<pll>;
/******** type define END ********/

/******** const BEGIN ********/
constexpr char ln  = '\n';
constexpr char sp  = ' ';
constexpr ld PI        = 3.141592653589793238462643383279502884197169399375105820974944;
// 0 ~ 3 -> UDLR, 4 ~ 7 -> (diag)UDLR, 8 ~ 15 -> knight
constexpr int dy[] = {-1,1,0,0,-1,-1,1,1,-2,-1,1,2,2,1,-1,-2};
constexpr int dx[] = {0,0,-1,1,-1,1,-1,1,1,2,2,1,-1,-2,-2,-1};
/******** const END ********/

/******** DEBUG TEMPLATE BEGIN ********/
#ifdef LOCAL
void _DEBUG_S(string _s="") { cerr << "\n[------- " << _s << " ---------]\n"; }
template<typename Type> void _DEBUG(Type arg) { cerr << arg; }
template<typename Type, typename... Types> void _DEBUG(Type arg, Types ...args) { cerr << arg << ", ", _DEBUG(args...); }
#define debug(...) cerr << "[ " << #__VA_ARGS__ << " ] : ", _DEBUG(__VA_ARGS__)
#define debug2(...) _DEBUG_S("DEBUG BEGIN") debug(__VA_ARGS__) _DEBUG_S("DEBUG END")

#else
#define debug(...)
#define debug2(...)
#endif 
/******** DEBUG TEMPLATE END ********/

/******** I/O TEMPLATE BEGIN ********/
template<int fp=0> struct fastio{ fastio(){ 
#ifndef LOCAL
    if(fp>=0) { ios::sync_with_stdio(false); cin.tie(0); }
#endif 
    if(fp>0)cout << fixed << setprecision(fp); 
} };

template<typename Type> void input(Type &arg){cin >> arg;}
template<typename Type, typename... Types> void input(Type &arg, Types &...args){cin>>arg;input(args...);}
template<typename Type> void output(Type arg){cout<<arg;}
template<typename Type, typename... Types> void output(Type arg, Types ...args){cout<<arg;output(args...);}
template<typename T1, typename T2> inline istream& operator>>(istream &in, pair<T1, T2> &_p) { in >> _p.first >> _p.second; return in; }
template<typename T1, typename T2> inline ostream& operator<<(ostream &out, const pair<T1, T2> &_p) { out << _p.first << ' ' << _p.second; return out; }
template<typename Type> inline ostream& operator<<(ostream &out, const vector<Type> &v) { for(auto &i: v) out<<i<<' '; return out; }
template<typename Type> inline istream& operator>>(istream &in, vector<Type> &v)       { for(auto &i: v) in>>i; return in; }
template<typename Type> inline ostream& operator<<(ostream &out, const deque<Type> &v) { for(auto &i: v) out<<i<<' '; return out; }
template<typename Type> inline istream& operator>>(istream &in, deque<Type> &v)       { for(auto &i: v) in>>i; return in; }
/******** I/O TEMPLATE END ********/

template<typename T>
T power(T a, T b, T mod=numeric_limits<T>::max()){
    if(b == 0)return 1;
    if(b % 2)return a * power(a, b-1, mod) % mod;
    return power(a * a % mod, b >> 1, mod);
}
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }
ll extgcd(ll a, ll b, ll &x, ll &y){
    if(b) {
        ll d = extgcd(b, a % b, y, x);
        return y -= a / b * x, d;
    }
    return x = 1, y = 0, a;
}
/****************************************************************************************************************************/
/*************************************                   My Template End                *************************************/
/****************************************************************************************************************************/

#include<sys/time.h>
long getSeed() {
    struct timeval tick;
    gettimeofday(&tick, 0);
    return tick.tv_usec;
}

int gen(int mn, int mx){
    assert(mn <= mx);
    return rand() % (mx - mn + 1) + mn;
}

string gen(int len){
    string ret = "";
    while(len--){
        ret += (char)('a' + gen(0, 25));
    }
    return ret;
}

set<pair<int, int>> problems;

int main(){
    fastio<>();

    srand(getSeed());
    string s;
    int mx = 0;
    while(cin >> s){
        // 1 ~ 15
        auto it = s.find("$", 0);
        int number = stoi(s.substr(0, it));
        int level  = stoi(s.substr(it + 1));
        mx = max(mx, number);
        if(1 <= level && level <= 15) problems.emplace(level, number);
    }

    //  1 ~  8 1
    //  9 ~ 12 2
    // 13 ~ 15 1
    
    vector<pair<int, int>> L;
    L.emplace_back( 1,  8); // B5 ~ S3
    L.emplace_back( 9, 12); // S2 ~ G4
    L.emplace_back( 9, 12); // S2 ~ G4
    L.emplace_back(13, 15); // G3 ~ G1
    
    vector<pair<int, int>> output;
    for(auto &[l, r]: L){
        int level = gen(l, r);
        int problem = gen(1000, mx);
        auto it = problems.lower_bound(make_pair(level, problem));
        if(it->first != level && it != problems.begin()) it--;
        output.emplace_back(it->first, it->second);
        problems.erase(it);
    }
    sortall(output);
    for(auto &i: output) cout << i.second << '\n';

    return 0;
}
