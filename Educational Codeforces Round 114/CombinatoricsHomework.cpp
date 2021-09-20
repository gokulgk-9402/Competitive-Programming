#include<iostream>
using namespace std;

int main() {
    int t;
    long int a,b,c,m;
    long int ta,tb,tc;
    cin>>t;
    while (t>0) {
        cin>>a>>b>>c>>m;
        ta=a==0?a:a-1;
        tb=b==0?b:b-1;
        tc=c==0?c:c-1;
        if ((ta+tb+tc>=m)&&(a-b-c-1<=m)&&(b-a-c-1<=m)&&(c-a-b-1<=m)) 
            cout<<"YES\n";
        else
            cout<<"NO\n";
        t--;
    }
    return 0;
}