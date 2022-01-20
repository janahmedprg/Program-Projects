#include<iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int te = 0; te<t;te++){
        int a,b,c;
        cin>>a>>b>>c;

        int d1 = b-a;
        int d2 = c-b;
        int d3 = (c-a)/2;

        if(b+d1!=0 && (b+d1)%c==0){
            if((b+d1)/c>0){
                cout<<"YES"<<endl;
                continue;
            }
        }

        if((b-d2)!=0 && (b-d2)%a==0){
            if((b-d2)/a>0){
                cout<<"YES"<<endl;
                continue;
            }
        }

        if((a+d3)!=0 && (a+d3)%b==0){
            if((c-a)%2==1 || (a-c)%2==1){
                cout<<"NO"<<endl;
                continue;
            }
            if((a+d3)/b>0){
                cout<<"YES"<<endl;
                continue;
            }
        }
        cout<<"NO"<<endl;
    }
    return 0;
}