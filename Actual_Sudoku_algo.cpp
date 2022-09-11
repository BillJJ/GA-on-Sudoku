#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
#pragma GCC target("avx2")
typedef long long ll;
typedef pair<int, int> pii;

const int MM = 2e5+5;

char a[9][9];

pii boxes[9][9], stk[82];
int idx=0, stop=0;

bool done = 0;
void f(){
    if(done) return;
    if(idx == stop){
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                cout << a[i][j];
            }
            cout << "\n";
        }
        done = 1;
        return;
    }

    auto[x, y] = stk[idx];

    vector<bool> vis (10);
    for(int i = 0; i < 9; i++) if(a[x][i] != '.') vis[a[x][i]-'1'] = 1;
    for(int i = 0; i < 9; i++) if(a[i][y] != '.') vis[a[i][y]-'1'] = 1;
    for(auto[i, j] : boxes[(x/3)*3 + y/3]) if(a[i][j] != '.') vis[a[i][j]-'1'] = 1;

    idx++;
    for (int i = 0; i < 9; i++) {
        if(vis[i]) continue;

        a[x][y] = i+'1';
        f();
        a[x][y] = '.';
    }
    idx--;

    return;
}

signed main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    for(int i = 0; i < 9; i++){
        for(int j = 8; j >= 0; j--){
            boxes[(i/3)*3 + j/3][(i%3)*3 + (j%3)] = {i,j};
        }
    }

    for(auto &v : a) for(char &c : v) cin >>c;

    for (int i = 0; i <9 ; ++i) {
        for(int j= 0;j<9;j++){
            if(a[i][j]=='.') stk[stop++] = {i,j};
        }
    }
    
    f();

    return 0;
}
