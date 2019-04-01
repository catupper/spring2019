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
void view_vector(vector<Int> v){
  for(Int i = 0;i < v.size();i++)
    cout << v[i] << " ";
  cout << endl;
}

//全探索
void solveAll(Int N, Int W, vector<Int> v, vector<Int> w){
  vector<Int> vsum(1 << N, 0), wsum(1 << N, 0);
  Int ans = 0;
  for(Int i = 1;i < (1 << N);i++){
    Int l = i & -i;
    int k = 0;
    while((1 << k) != l)k++;
    vsum[i] = vsum[i - l] + v[k];
    wsum[i] = wsum[i - l] + w[k];
    if(wsum[i] <= W && vsum[i] > vsum[ans]){
      ans = i;
    }
  }
  cout << "V:" << vsum[ans] << " W:" << wsum[ans] << endl;
  for(Int i = 0;i < N;i++){
    if((ans >> i) % 2)cout << i << " ";
  }cout << endl;
}

//動的計画法
void solveDP(Int N, Int W, vector<Int> v, vector<Int> w){
  vector< Int > dp(W+1, 0);
  for(Int i = 0;i < N;i++){
    for(Int j = W;j >= w[i];j--){
      dp[j] = max(dp[j], dp[j-w[i]] + v[i]);
    }
  }
  cout << dp[W] << endl;
}


int main(){
  Int N, W;
  cin >> N >> W;
  vector<Int> v(N), w(N);
  for(Int i = 0;i < N;i++){
    cin >> v[i] >> w[i];
  }

  //solveAll(N, W, v, w);
  solveDP(N, W, v, w);
}
