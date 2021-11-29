// Authored by : fltcy2039
// Co-authored by : -
// Link : http://boj.kr/fd177f1f686d409484f231c8b81ca146

#include <bits/stdc++.h>
using namespace std;
int arr[100005];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    //input & init
    int N; cin >> N;
    for(int i = 0 ; i < N; i++) cin >> arr[i];
    
    int min;
    int start, end, answer_start, answer_end;
    
    //process
    sort(arr, arr + N);
    
    //답 후보 인덱스 answer_start, answer_end
    //갱신을 위해 이동하는 인덱스 start, end
    answer_start = start = 0;
    answer_end = end = N - 1;
    min = abs(arr[start]+arr[end]);
        
    int sum = min;
    while(start < end){
        sum = arr[start] + arr[end];
        if(min > abs(sum)){
            min = abs(sum);
            answer_start = start;
            answer_end = end;
        }
        
        //절댓값을 줄이는 방향으로 인덱스 이동
        if(sum < 0) start++;
        else end--;
    }
    
    //output
    cout << arr[answer_start] << " "<< arr[answer_end] << "\n";
    return 0;
}
