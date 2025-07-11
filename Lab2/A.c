#include <stdio.h>

void find_target_sum(int arr[],int target,int length_of_arr)
{
    int low=0,high=length_of_arr-1,mid,output[2],check,flag=0;
    while (low < high)
    {
        check = arr[low]+arr[high];
        if (check == target)
        {
            printf("%d %d",low+1,high+1);
            flag = 1;
            break;
        }
        else if (target>check)
        {
            low++;
        }
        else if (target < check)
        {
            high--;
        }
    }
    if (flag == 0)
    {
        printf("-1");
    }
}
int main()
{

    int length_of_arr,target;
    scanf("%d %d",&length_of_arr,&target);
    int arr[length_of_arr];
    for (int i=0;i<length_of_arr;i++)
    {
        scanf("%d",&arr[i]);
    }
    find_target_sum(arr,target,length_of_arr);
    return 0;
}
