#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
#define INF (1LL << 60)
typedef long long Int;

//vectorの表示
template<typename T>
ostream& operator<<(ostream& stream, vector<T>& container){
  for(auto elem:container)stream << elem << " ";
  return stream;
}
void view_vector(vector<int> v){
  for(int i = 0;i < v.size();i++)
    cout << v[i] << " ";
  cout << endl;
}

//全探索
void solveAll(int n, vector<vector<int> > d){
  vector<int> route, min_route;
  Int min_dist = 1LL<<60;
  for(int i = 1;i < n;i++)route.push_back(i);
  do{
    Int tmp = d[0][route[0]];
    for(int i = 0;i+1 < route.size();i++){
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


void solveDP(int n, vector<vector<int> > d){
  vector< vector<Int> > dp(1<<n, vector<Int>(n, INF));
  vector< vector<Int> > before(1<<n, vector<Int>(n, 0));
  dp[1][0] = 0;
  for(int i = 1;i < (1<<n);i++){
    for(int j = 0;j < n;j++){
      if((i>>j)%2 == 0)continue;
      for(int k = 1;k < n;k++){
        if((i>>k)%2 == 1)continue;
        int nxti = i + (1 << k);
        if(dp[i][j] + d[j][k] < dp[nxti][k]){
          dp[nxti][k] = dp[i][j] + d[j][k];
          before[nxti][k] = j;
        }
      }
    }
  }
  Int ans = INF;
  Int last = -1;
  for(int i = 1;i < n;i++){
    Int tmp = dp[(1<<n)-1][i] + d[i][0];
    if(ans > tmp){
      ans = tmp;
      last = i;
    }
  }
  vector<Int> min_route = {0};
  int now = (1<<n)-1;
  for(int i = last;i != 0;){
    min_route.push_back(i);
    int nxti = before[now][i];
    now -= 1 << i;
    i = nxti;
  }
  min_route.push_back(0);
  reverse(min_route.begin(), min_route.end());
  cout << ans << endl;
  cout << min_route << endl;

}

int main(){
  Int n;
  cin >> n;
  vector<vector<int> > d(n, vector<int>(n));
  for(int i = 0;i < n;i++){
    for(int j = 0;j < n;j++){
      cin >> d[i][j];
    }
  }

  solveAll(n, d);
  solveDP(n, d);
}
