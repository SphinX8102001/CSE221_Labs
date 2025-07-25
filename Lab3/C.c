#include <stdio.h>
#include <math.h>
int main()
{
    long long a,b,result=1;
    scanf("%lld %lld",&a,&b);
    while (b > 0)
    {
        if ( b % 2 == 1)
        {
            result = (result * a) % 107;
        }
        a = (a * a) % 107;
        b = b / 2;
    }
    result = result % 107;
    printf("%lld",result);
    return 0;
}
