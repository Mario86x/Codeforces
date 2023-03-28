#include<bits/stdc++.h>
#include<iostream>
using namespace std;

string outvalue(int* a, int* b, int n){

    for (int i=0;i<n;i++){
        if ((a[n-1]<a[i] || b[n-1]<b[i]) && (b[n-1]<a[i] || a[n-1]<b[i]))
            return "No\n";
        //if (a[n-1]>=a[i] && b[n-1]>=b[i]) || (b[n-1]>=a[i] && a[n-1]>=b[i])
    }
    return "Yes\n";
}
int main() {
    int a[100],b[100]; 
    int n=0;
    int n_test_cases;
    cin >> n_test_cases;
    for (int j=0; j<n_test_cases;j++){
        cin >> n;
        for (int i=0;i<n;i++){
            cin >> a[i];
        }
        for (int i=0;i<n;i++){
            cin >> b[i];
        }
        cout << outvalue(a,b,n);
    }
}

/*    
    for (int )*/