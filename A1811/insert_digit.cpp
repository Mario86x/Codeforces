#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int char2int(char c) {
    return c-'0';
}

char int2char(int k){
    return k+'0';
}


int test_case(char *p) {
    int n;
    cin >> n;
    // cout << "n = " << n << endl;
    int d_int;
    cin >> d_int;
    // cout << "d = " << d_int << endl;
    char d = int2char(d_int);
    char temp;
    bool inserted = false;
    for (int i=0; i<n; i++){
        cin >> temp;
        if (temp<d && inserted==false) {
            *(p+i)=d;
            inserted=true;
        }
        *(p+i+inserted)=temp;
        if (i==n-1 && inserted == false)
            *(p+i+1)=d;
    }
    for (int i=0; i<n+1; i++) {
        cout << *(p+i);
    }
    cout << endl;
    return n; //shift pointer by n+1
}



int main() {
    char vec[200001];
    char *p=vec;
    int t;
    cin >> t;
    while (t--){
        test_case(p);
    }
}
