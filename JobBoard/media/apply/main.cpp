#include <bits/stdc++.h>
using namespace std;


int main()
{
    long long n;
    cin>>n;
    for(long long i = 0; i < n; i++)
    {
        long long m, c, d, sum = 0;
        cin>>m>>c>>d;
        long long arr[m];
        for(long long j = 0; j < m; j++)
        {
            cin>>arr[j];
        }
        int it = sizeof(arr) / sizeof(arr[0]);
        sort(arr, arr + n);
        if(arr[m-1] * d < c)
        {
            cout<<"Impossible"<<endl;
        }
        else if (arr[m-1] > c)
        {
            cout<<"Infinity"<<endl;
        }
        else
        {
            long long q = 0, k = d, r;
            for(long long j = 0; j < d; j++)
            {
                if(q == m)
                {
                    q = 0;
                }
                sum += arr[q];
                q++;
            }
            if(m < d)
            {
                k = m;
            }
            else
                k = d;
            if(sum < c)
            {
                while(sum < c)
                {

                }
            }
        }
    }
}
return 0;
}
