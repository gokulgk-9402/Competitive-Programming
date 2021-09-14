#include<iostream>
using namespace std;

int main() {
    int t,n,s;

    cin>>t;
    while(t) {
        cin>>n>>s;
        if(n==1)
            cout<<s;
        else if (n==2)
            cout<<s/2;
        else if(n%2==0) {
            n=n/2+1;
            cout<<s/n;
        }
        else {
            n=n-n/2;
            cout<<s/n;
        }
        cout<<endl;
        t--;
    }
    return 0;
}
