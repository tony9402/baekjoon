#include <bits/stdc++.h>
using namespace std;

int main() {

   int n = 0;
   long long ans = 1;

   cin >> n;

   for (int i = 1; i <= n; i++) {
      ans *= i;
      ans %= 100000000;
      while (ans % 10 == 0) {
         ans /= 10;
      }
   }

   cout << ans % 10;

   return 0;
}