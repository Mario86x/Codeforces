#include<bits/stdc++.h>
#include<iostream>
using namespace std;

void test_case() {
    int n;
    cin >> n;
    vector<unsigned long int> b(n-1);
    for (int i=0;i<n-1;i++){
        cin >> b[i];
    }
    cout << b[0] << " ";
    for (int i=0;i<n-2;i++){
        cout << min(b[i],b[i+1]) << " ";
    }
    cout << b[n-2] << endl;
}

int main() {
    int t;
    cin >> t;
    while ((t--) > 0){
        test_case();
    }
}