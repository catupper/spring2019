#include<iostream>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<time.h>

using namespace std;
#define INF (1LL << 60)
typedef long long Int;

//vectorの表示
template<typename T>
ostream& operator<<(ostream& stream, vector<T>& container){
  for(auto elem:container)stream << elem << " ";
  return stream;
}
void view_vector(vector<Int> v){
  for(Int i = 0;i < v.size();i++)
    cout << v[i] << " ";
  cout << endl;
}

//全探索
void solveAll(Int n, vector<vector<Int> > d){
  vector<Int> route, min_route;
  Int min_dist = 1LL<<60;
  for(Int i = 1;i < n;i++)route.push_back(i);
  do{
    Int tmp = d[0][route[0]];
    for(Int i = 0;i+1 < route.size();i++){
      tmp += d[route[i]][route[i+1]];
    }
    tmp += d[route.back()][0];
    if(tmp < min_dist){
      min_dist = tmp;
      min_route = route;
    }
  }while(next_permutation(route.begin(), route.end()));
  cout << min_dist << endl;
  cout << "0 " << min_route << "0" << endl;
}

//動的計画法
void solveDP(Int n, vector<vector<Int> > d){
  vector< vector<Int> > dp(1<<n, vector<Int>(n, INF));
  vector< vector<Int> > before(1<<n, vector<Int>(n, 0));
  dp[1][0] = 0;
  for(Int i = 1;i < (1<<n);i++){
    for(Int j = 0;j < n;j++){
      if((i>>j)%2 == 0)continue;
      for(Int k = 1;k < n;k++){
        if((i>>k)%2 == 1)continue;
        Int nxti = i + (1 << k);
        if(dp[i][j] + d[j][k] < dp[nxti][k]){
          dp[nxti][k] = dp[i][j] + d[j][k];
          before[nxti][k] = j;
        }
      }
    }
  }
  Int ans = INF;
  Int last = -1;
  for(Int i = 1;i < n;i++){
    Int tmp = dp[(1<<n)-1][i] + d[i][0];
    if(ans > tmp){
      ans = tmp;
      last = i;
    }
  }
  vector<Int> min_route = {0};
  Int now = (1<<n)-1;
  for(Int i = last;i != 0;){
    min_route.push_back(i);
    Int nxti = before[now][i];
    now -= 1 << i;
    i = nxti;
  }
  min_route.push_back(0);
  reverse(min_route.begin(), min_route.end());
  cout << ans << endl;
  cout << min_route << endl;
}

//焼きなまし法
void solveAnealing(Int n, vector<vector<Int> > d){
  vector<Int> min_route, route;
  Int tmp = 0;
  for(Int i = 0;i < n;i++){
    route.push_back(i);
    tmp += d[i][(i+1)%n];
  }
  Int ans = tmp;
  min_route = route;

  Int LOOP = 10000000, K = 10;
  for(Int i = 0;i < LOOP;i++){
    Int a = rand() % n;
    Int b = rand() % n;
    if(a > b)swap(a, b);
    if((b+1)%n == a || a == b)continue;
    Int tmp2 =tmp;
    tmp2 += -d[route[(a+n-1)%n]][route[a]] + d[route[(a+n-1)%n]][route[b]];
    tmp2 += -d[route[b]][route[(b+1)%n]] + d[route[a]][route[(b+1)%n]];
    if(tmp2 < tmp || rand() % (LOOP * K) < 10){
      tmp = tmp2;
      reverse(route.begin() + a, route.begin() + b + 1);
    }
    else continue;
    if(tmp < ans){
      ans = tmp;
      min_route = route;
    }
  }
  cout << ans << endl;
  cout << min_route  << min_route[0] << endl;
}

int main(){
  srand((unsigned) time(NULL));
  Int n;
  cin >> n;
  vector<vector<Int> > d(n, vector<Int>(n));
  for(Int i = 0;i < n;i++){
    for(Int j = 0;j < n;j++){
      cin >> d[i][j];
    }
  }

  //solveAll(n, d);
  //solveDP(n, d);
  solveAnealing(n, d);
}
