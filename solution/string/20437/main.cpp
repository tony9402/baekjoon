//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/d7d7acc92493486db20da4343b0747e0

/* 
문제 조건
3. 어떤 문자를 정확히 K개 포함하는 가장 짧은 문자열
== 시작과 끝이 어떤 문자인 가장 짧은 문자열
4. 어떤 문자를 정확히 K개를 포함하고 어떤 문자가 시작과 끝인 가장 긴 문자열
== 시작과 끝이 어떤 문자인 가장 긴 문자열
*/

#include <bits/stdc++.h>

using namespace std;
int alpha[26];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        //alpha 배열을 초기화 합니다.
        for(int i = 0;i < 26;i++)
            alpha[i] = 0;
        
        string W;
        int K;
        cin >> W >> K;
        
        //입력받은 문자열의 알파벳을 기록합니다.
        for(int i = 0;i < W.length();i++)
            alpha[W[i] - 'a']++;
        
        //K보다 크거나 같은 빈도로 나온 알파벳에
        //대해서만 검사합니다.
        int _min = INT_MAX, _max = 0;
        for(int i = 0;i < W.length();i++){
            if(alpha[W[i] - 'a'] < K) continue;

            //그 알파벳을 시작과 끝으로 생각하고
            //그 알파벳이 정확히 K개가 나왔을 때 문자열의 길이를
            //기존의 _max와 _min값과 비교하여 업데이트 합니다.
            int count = 0;
            for(int j = i;j < W.length();j++){
                if(W[i] != W[j]) continue;
                else count++;

                if(count == K){
                    _min = min(_min, j - i + 1);
                    _max = max(_max, j - i + 1);
                    break;
                }
            }
        }
        if(_min > 10001 || _max == 0) cout << "-1\n";
        else cout << _min << " " << _max << '\n';
    }
    return 0;
} 
