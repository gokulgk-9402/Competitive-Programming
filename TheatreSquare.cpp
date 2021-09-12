#include<iostream>
using namespace std;

int main() {
    long long int m,n,a;
    long long int x,y;
    cin>>m>>n>>a;
    x=m/a;
    y=n/a;
    if(m%a!=0)
        x+=1;
    if(n%a!=0)
        y+=1;
    cout<<x*y<<endl;
    return 0;
}