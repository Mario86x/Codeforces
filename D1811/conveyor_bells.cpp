#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int maxnorm(long x,long y,long n){
    return max(abs((x-n/2-(x<=n/2))),abs((y-n/2-(y<=n/2))));
}

void test_case() {
    long int n,x1,y1,x2,y2;
    cin >> n >> x1 >> y1 >> x2 >> y2;
    cout << abs(maxnorm(x1,y1,n) - maxnorm(x2,y2,n)) << endl;
}



int main() {
    int t;
    cin >> t;
    while (t--){
        test_case();
    }
}
