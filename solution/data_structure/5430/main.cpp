//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c58e7826ebb34f06b1a2e42cfd4e5deb

/*
시간이 빡빡해서 실제로 뒤집기, 삭제하기를 구현하면 안됩니다.
뒤집기는 실제로 뒤집는 것이 아닌 앞에서 뒤로 읽는걸 뒤에서 앞으로 읽게 하였고
삭제하기는 실제 삭제가 아닌 front포인터를 하나 증가시키는 식으로 구현했습니다.
*/

#include <bits/stdc++.h>

using namespace std;

void inputString(string str);
void reverseList();
void outputList();
bool deleteList();

vector<string> numlist;
bool _reverse = false;
int front, back;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        string p, arr;
        int n;
        cin >> p >> n >> arr;

        inputString(arr);

        //실행할 함수를보고 적절하게 구현
        bool error = false;
        for(int i = 0;i < p.length();i++){
            if(p[i] == 'R')
                reverseList();
            else {
                if(deleteList() == false) {
                    cout << "error" << '\n';
                    error = true;
                    break;
                }
            }
        }
        if(error == false) outputList();
        numlist.clear();
        _reverse = false;
    }

    return 0;
} 

//비어있는 상황 []도 출력을 할 경우가 있기 때문에
//for문 안에 마지막 숫자는 컴마(,)를 출력하지 않도록 하였습니다.
void outputList(){
    cout << '[';
    if(_reverse == false){
        for(int i = front;i <= back;i++){
            if(i == back) cout << numlist[i];
            else cout << numlist[i] << ",";
        }
    }
    else{
        for(int i = back;i >= front;i--){
            if(i == front) cout << numlist[i];
            else cout << numlist[i] << ",";
        }
    }
    cout << "]\n";
}

//뒤집혀 있는 상태에서는 back이 앞쪽이 됩니다.
//따라서 back크기를 하나 줄여줍니다.
//추가로 front > back 일때 error상황을 체크합니다.
bool deleteList(){
    if(front > back) return false;
    else {
        if(_reverse == false) front++;
        else back--;

        return true;
    }
}

//_reverse가 true면 뒤집혀있다 라고 생각합니다.
void reverseList(){
    if(_reverse == true) _reverse = false;
    else _reverse = true;
}

//문자열을 뒤에서부터 읽으며 숫자만 numlist에 넣습니다.
void inputString(string arr){
    string num = "";
    while(!arr.empty()){
        if(arr.back() >= '0' && arr.back() <= '9'){
            num += arr.back();
            arr.pop_back();
        }
        else{
            if(num.empty() == true)
                arr.pop_back();
            else{
                reverse(num.begin(), num.end());
                numlist.push_back(num);
                num = "";
                arr.pop_back();
            }
        }
    }
    
    reverse(numlist.begin(), numlist.end());

    front = 0;
    back = numlist.size() - 1;
}
