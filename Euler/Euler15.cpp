#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MOD = 1000000007;
const int MAX = 1007;
int grid [MAX][MAX];

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    grid [0][0] = 1;
    for(int i =1; i <MAX; ++i){
        grid[i][0] = 1;
        for(int j =1; j<=i ; ++j){
            grid[i][j]=(grid[i-1][j-1]+grid[i-1][j])%MOD;
        }
    }

    int T,N,M;
    cin >> T;
    while(T--){
        cin >> N >> M;
        cout << grid[N+M][N];
    }

    return 0;
}

