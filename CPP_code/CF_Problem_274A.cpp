#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    vector<int> v;
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());
    vector<int> f;
    f.push_back(v[0]);
    for(int i=1;i<n;i++){
        bool isK = false;
        if(v[i]%k!=0){
            f.push_back(v[i]);
            continue;
        }
        int j= 0;
        for (int b = f.size()/2; b >= 1; b /= 2) {
            while (j+b < f.size() && f[j+b] <= v[i]/k) j += b;
        }
        if (f[j] == v[i]/k) {
            isK = true;
        }
        if(!isK){
            f.push_back(v[i]);
        }
    }
    cout<<f.size()<<endl;
    return 0;
}