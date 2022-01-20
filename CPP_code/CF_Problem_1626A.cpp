#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        string s;
        cin>>s;
        sort(s.begin(), s.end());
        cout << s << endl;;
    }
    return 0;
}