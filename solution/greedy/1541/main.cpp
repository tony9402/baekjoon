//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/947894d11f12498d993f44e29759788b

#include <bits/stdc++.h>

using namespace std;
vector<string> vec;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    string input;
    cin >> input;

    //입력받은 문자열을 숫자와 기호로 나누어
    //벡터에 저장합니다.
    //기호를 만나는 지점에 만들어졌던 숫자를 저장합니다.
    string num = "";
    for(int i = 0;i < input.length();i++){
        if(input[i] >= '0' && input[i] <= '9')
            num += input[i];
        else{
            vec.push_back(num);
            string s;
            s = input[i];
            vec.push_back(s);
            num = "";
        }
    }
    //끝이 숫자로 끝나므로 마지막 숫자를 벡터에 저장
    vec.push_back(num);

    //첫 숫자는 반드시 더합니다.
    //두번째 숫자부터는 첫 마이너스를 만나기 전까지는 더하고
    //첫 마이너스를 만나는 순간부터 뒤 숫자는 모두 빼주어야 최소값이 됩니다.
    //이유는 어떻게든 괄호를 쳐서 빼기를 할 수 있습니다.
    bool minus = false;
    int sum = 0;
    sum += stoi(vec[0]);
    for(int i = 1;i < vec.size();i++) {
        if(vec[i] == "+") continue;
        else if(vec[i] == "-") minus = true;
        else{
            if(minus == true) sum -= stoi(vec[i]);
            else sum += stoi(vec[i]);
        }
    }

    cout << sum;

    return 0;
} 
