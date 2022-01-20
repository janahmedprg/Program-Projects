#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        vector<int> v;
        int n;
        cin>>n;
        for (int i= 0;i<n;i++){
            int el;
            cin>>el;
            v.push_back(el);
        }
        sort(v.begin(),v.end());
        int diff = v[v.size()-1]-v[0];
        cout<<diff<<endl;
    }
    return 0;
}