#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        int n,l;
        cin>>n>>l;
        int w[l];
        int fin=0;
        for(int i=0;i<l;i++){
            w[i]=0;
        }
        for(int i= 0;i<n;i++){
            int x;
            cin>>x;
            for(int j = 0;j<l;j++){
                w[j] += x%2;
                x = x/2;
            }
        }
        for (int i=0;i<l;i++){
            int a;
            if(double(w[i])/n<=0.5){
                a = 0;
            }
            else{
                a=2;
                fin += pow(a,i);
            }
        }
        cout<< fin<<endl;
    }
    return 0;
}