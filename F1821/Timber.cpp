#include<bits/stdc++.h>
#include<iostream>
#include<cmath>
using namespace std;

const unsigned long modn = 998244353;

unsigned long powerm2(int m){
    if (m==0)
        return 1;
    else
        return powerm2(m-1)*2 % modn;
}
unsigned long nways(int n,int m,int k);

unsigned long ionways(int n, int m, int k){
    if (n<=0)
        return 0;
    else
        return nways(n,m,k) - ionways(n-k,m,k);
}


unsigned long nways(int n,int m,int k) {
    if (n<0)
        return 0;
    if (m==0)
        return 1;
    if (n==0)
        return 0;
    if (m*(k+1) > n)
        return 0;
    if (m*(k+1) == n) {
        //cout << "checkpoint" << n << m << k << endl;
        return powerm2(m);
    }
    else
        return ((nways(n-1,m,k) % modn) + (2*nways(n-k-1,m-1,k) % modn) - (nways(n-2*k-1,m-1,k) % modn)) % modn;
}

int main() {
    int n,m,k;
    cin >> n >> m >> k;
    cout << nways(n,m,k) << endl;
    return 0;
}