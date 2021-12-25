// Authored by : xhdxhl
// Co-authored by : -
// Link : http://boj.kr/86c226302ae94672947f1600061f2976
#include <bits/stdc++.h>

using namespace std;

int result, nums[10], flag;
string word = "helowrd";
unordered_map <char, int> m;

int main(){
    ios_base::sync_with_stdio(0); 
    cin.tie(0); cout.tie(0);
    
    cin >> result;
    for(int i = 0; i < 10; i++) nums[i] = i;

    do{
        for(int i = 0; i < word.size(); i++) m[word[i]] = nums[i];

        if(m['h'] == 0 || m['w'] == 0) continue;

        int a = m['h'] * 10000 + m['e'] * 1000 + m['l'] * 100 + m['l'] * 10 + m['o'];
        int b = m['w'] * 10000 + m['o'] * 1000 + m['r'] * 100 + m['l'] * 10 + m['d'];

        if(a + b == result){
            int as = to_string(a).size();
            int bs = to_string(b).size();
            
            cout << "  " << a << '\n';
            cout << "+ " << b << '\n';
            cout << "-------\n";
            for(int i = 0; i < 7 - to_string(result).size(); i++) cout << ' ';
            cout << result << '\n';
            
            flag = 1;
            break;
        }

    } while(next_permutation(nums, nums + 10));
    
    if(!flag) cout << "No Answer";
}
