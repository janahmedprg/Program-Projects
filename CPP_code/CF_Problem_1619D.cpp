#include<iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int tests;
    cin>>tests;

    for(int t=0;t<tests;t++){
        int n,m;
        cin>>m>>n;
        int joys[m][n];
        for (int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                int joy;
                cin>>joy;
                joys[i][j] = joy;
            }
        }
        if ((n-1)>m){
            int topByFriends[n];
            for (int i=0; i<n;i++){
                int top=0;
                for (int j=0;j<m;j++){
                    if(joys[j][i]>top){
                        topByFriends[i]=joys[j][i];
                        top=joys[j][i];
                    }
                }
            }
            int minByFriends = 1e9+9;
            for(int i=0;i<n;i++){
                if(topByFriends[i]<minByFriends){
                    minByFriends = topByFriends[i];
                }
            }
            cout<<minByFriends<<endl;
        }
        else{
            int topByFriends[n];
            for (int i=0; i<n;i++){
                int top=0;
                for (int j=0;j<m;j++){
                    if(joys[j][i]>top){
                        top=joys[j][i];
                    }
                }
                topByFriends[i]=top;
            }
            
            int minByFriends = 1e9+9;
            for(int i=0;i<n;i++){
                if(topByFriends[i]<minByFriends){
                    minByFriends = topByFriends[i];
                }
            }
            int top2ByShops[m];
            for(int i=0;i<m;i++){
                int tmpMax=0;
                top2ByShops[i]=0;
                for (int j=1;j<n;j++){
                    if(joys[i][j]>joys[i][tmpMax]){
                        tmpMax = j;
                    }
                }
                for(int j=0;j<n;j++){
                    if(j==tmpMax){
                        continue;
                    }
                    if(joys[j][i]>top2ByShops[i]){
                        top2ByShops[i]=joys[i][j];
                    }
                }
            }
            int maxtop2ByShops=0;
            for(int i=0;i<m;i++){
                if(top2ByShops[i]>maxtop2ByShops){
                    maxtop2ByShops=top2ByShops[i];
                }
            }
            cout<<min(maxtop2ByShops,minByFriends)<<endl;
        }
    }
    
    return 0;
}