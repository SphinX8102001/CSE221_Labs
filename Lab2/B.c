#include <stdio.h>
int computation(int A[],int B[],int n,int m,int target)
{
    int sum,low,high,l,difference;
    low = 0;
    high = m-1;
    int output[3]={__INT_MAX__,0,0};
    int k = 0;
    while (low<n && high>=0)
    {
        sum = A[low] + B[high];
        difference = abs(sum - target);
        if (difference < output[0])
        {
            output[0] = difference;
            output[1] = low;
            output[2] = high;

        }

        if (difference == 0)
        {
            printf("%d %d",low+1,high+1);
            return 0;
        }
        else if (sum > target)
        {
            high--;
        }
        else if (sum < target)
        {
            low++;
        }
    }


    printf("%d %d",output[1]+1,output[2]+1);
    return 0;

}
int main()
{
    int n,m,target_sum;
    scanf("%d %d %d",&n,&m,&target_sum);
    int A[n],B[m];
    for (int i=0;i<n;i++)
    {
        scanf("%d",&A[i]);
    }
    for (int j=0;j<m;j++)
    {
        scanf("%d",&B[j]);
    }
    computation(A,B,n,m,target_sum);

}
