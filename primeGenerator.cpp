#include <bits/stdc++.h>
using namespace std;

int isprime(int);
 
int main()
{
    long int i,num,m,n,t;
    cin>>t;
    while(t) {
        cin>>m>>n;
        for(m;m<=n;m++) {
            if (isprime(m))
                cout<<m<<"\n";
        }
        cout<<"\n";
        t--;
    }    
    return 0;
}
 
int isprime(int n) {
    if (n==1)
        return 0;
    for (long int i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return 0;
    return 1;
}
