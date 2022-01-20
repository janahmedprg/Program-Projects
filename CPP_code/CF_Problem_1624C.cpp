#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        int a,n;
        cin>>n;
        vector<int> v;
        bool isPerm = true;
        int g[n];
        for(int i =0;i<n;i++){
            g[i]=0;
        }
        for (int i=0;i<n;i++){
            cin>>a;
            while(true){
                if(a<=n){
                    if(a==0){
                        isPerm = false;
                        break;
                    }
                    if(g[a-1]==0){
                        g[a-1] = 1;
                        break;
                    }
                }
                a=a/2;
            }
        }
        if(isPerm){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}