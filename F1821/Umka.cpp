#include<bits/stdc++.h>
#include<iostream>
using namespace std;

void generateFibVec(int n, long* fib){
    for (int i=0;i<n;i++){
        if (i==0) fib[i]=1;
        else if (i==1) fib[i]=1;
        else if (i>1) fib[i]=fib[i-1]+fib[i-2];
    }
}

void test_case() {
    int n;
    long x,y,Lx,Ly; //x Fn, y Fn+1
    cin >> n >> x >> y;
    long fib[n+2];
    generateFibVec(n+2,fib);
    Lx=fib[n];
    Ly=fib[n+1];
    // cout << x << "-" << y << "-"  << Lx << "-"  << Ly << "-"  << n << endl;
    for (int i=n;i>1;i--){
        // cout << x << "-" << y << "-"  << Lx << "-"  << Ly << "-"  << i << endl;
        if (x-fib[i]>0) {
            x=x-fib[i];
            Lx=Lx-fib[i];
        }
        else if (Lx-x-fib[i]>=0) {
            x=x;
            Lx=Lx-fib[i];
        }
        else if (y-fib[i]>0) {
            y=y-fib[i];
            Ly=Ly-fib[i];
        }
        else if (Ly-y-fib[i]>=0) {
            y=y;
            Ly=Ly-fib[i];
        }
        else {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--){
        test_case();
    }
}