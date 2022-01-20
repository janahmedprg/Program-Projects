#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        int x,a,b,xo;
        cin>>x;
        vector<int> v;
        int e = 0;
        xo=x;
        while(x/100>0){
            a = x%10;
            b = (x%100)/10;
            if ((a+b)<10){
                v.push_back((xo/(int)round(pow(10,2+e)))*(int)round(pow(10,1+e))+(a+b)*(int)round(pow(10,e))+xo%(int)round(pow(10,e)));
            }
            else{
                v.push_back((xo/(int)round(pow(10,2+e)))*(int)round(pow(10,2+e))+(a+b)*(int)round(pow(10,e))+xo%(int)round(pow(10,e)));
            }
            e+=1;
            x=x/10;
        }
        a = x%10;
        b = (x%100)/10;
        if ((a+b)<10){
            v.push_back((xo/(int)round(pow(10,2+e)))*(int)round(pow(10,1+e))+(a+b)*(int)round(pow(10,e))+xo%(int)round(pow(10,e)));
        }
        else{
            v.push_back((xo/(int)round(pow(10,2+e)))*(int)round(pow(10,2+e))+(a+b)*(int)round(pow(10,e))+xo%(int)round(pow(10,e)));
        }
        sort(v.begin(),v.end());
        cout<<v[v.size()-1]<<endl;
    }
    return 0;
}