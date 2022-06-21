#include<iostream>
using namespace std;

int main() {
    int t,n;
    int i,j;
    cin>>t;
    while (t>0) {
        cin>>n;
        for (i=n;i>0;i--) {
            for (j=i;j>0;j--) {
                cout<<"(";
            }
            for (j=i;j>0;j--) {
                cout<<")";
            }
            for (j=n-i;j>0;j--) {
                cout<<"(";
            }
            for (j=n-i;j>0;j--) {
                cout<<")";
            }
            cout<<"\n";
        }
        t--;
    }
    return 0;
}