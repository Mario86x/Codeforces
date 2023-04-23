#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int importer(int *n, int *A,int m){
    int *p = A;
    for (int i=0; i<m; i++){
        cin >> n[i];
        for (int j=0; j<n[i]; j++){
            cin >> *p;
            p++;
        }
    }
    return p-A;
    // for (int i=0; i<p-A; i++){
    //     cout << A[i] << ' ';
    // }
}

bool day_winner(int a_ij, int *A, int A_len){
    for (int j=0;j<A_len;j++){
        if (a_ij==A[j])
            return false;
    }
    return true;
}

int test_case() {
    int m;
    int n[50000],A[50001],winners[50000];
    int A_end;
    int *p;
    int i,j;

    cin >> m;
    A_end=importer(n,A,m);
    winners[m-1]=A[A_end-1];
    p=A; //reset p
    
    // cout << "*p = " << *p << " p-A = " << p-A << " A_len = " << A_end << endl;
    

    for (i=0;i<m-1;i++){
        for (j=0;j<n[i];j++){
            if (day_winner(*(p+j),p+n[i],A_end-(p-A+n[i]))){
                winners[i]=*(p+j);
                break;
            }
        }
        p+=n[i];

        if (j==n[i]){
            // cout << "no winner on day " << i << endl;
            cout << -1 << endl; //no winner for the day output -1
            break;
        }
    }
    if (i==m-1){
        for (j=0; j<m; j++){
            cout << winners[j] << ' ';
        }
        cout << endl;
    }
    return 0;
    
}


int main() {
    int t;
    cin >> t;
    for (int i=0;i<t;i++){
        test_case();
    }
}


