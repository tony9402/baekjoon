#include<iostream>
#include<string>
#include<stack>
#include<algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;

    stack<int> st;

    for(int i=0;i<N;i++){
        string cmd; cin >> cmd;
        if(cmd == "push") { //push X
            int X; cin >> X;
            st.push(X);
        }
        else if(cmd == "pop") {
            if(st.empty()) { //stack이 비어있다면,
                cout << -1 << '\n';
            }
            else {
                cout << st.top() << '\n';
                st.pop();
            }
        }
        else if(cmd == "size") {
            cout << (int)st.size() << '\n';
            // ✸  stack에서 size의 type은 size_t (unsigned int) 이다.
            //    이 문제에서는 문제가 안되지만 저 값에서 - 연산을 할 때 조심해야한다.
        }
        else if(cmd == "empty") {
            cout << st.empty() << '\n';
            // ✸  stack에서 empty의 type은 bool 이다.
            // true -> 1, false -> 0이 출력된다.
        }
        else if(cmd == "top") {
            if(st.empty()) {
                cout << -1 << '\n';
            }
            else {
                cout << st.top() << '\n';
            }
        }
    }
}
