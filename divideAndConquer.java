import java.util.*;

public class divideAndConquer{
  public static int maxCrossingSum(int array[],int low,int mid,int high){
    //Calculation of left sum
    int leftSum = Integer.MIN_VALUE;
    int sum = 0;
    for(int i=mid; i>=low; i--){
      sum += array[i];
      if(sum > leftSum){
        leftSum = sum;
      }
    }

    //Calculation of right sum
    int rightSum = Integer.MIN_VALUE;
    sum = 0;
    for(int j=mid+1; j<=high; j++){
      sum += array[j];
      if(sum > rightSum){
        rightSum = sum;
      }
    }

    return leftSum+rightSum;
  }

  static int maxSubArraySum(int array[], int low,
                                      int high)
    {
    int mid = (low + high)/2;
    // Base Case: Only one element
    if (low == high){
        return array[low];
    }else{
      int leftSum = maxSubArraySum(array,low,mid);
      int rightSum = maxSubArraySum(array,mid+1,high);
      int crossSum = maxCrossingSum(array,low,mid,high);
      if(leftSum >= rightSum && leftSum >= crossSum){
        return leftSum;
      }else if(rightSum >= leftSum && rightSum>= crossSum){
        return rightSum;
      }else{
        return crossSum;
      }
    }
    }

  public static void main(String args[]){
    int arr[] = {-2,-3,-5,4,-6,9,10,-3-5};
        int n = arr.length;
        int maxSum = maxSubArraySum(arr, 0, n-1);

        System.out.println("Maximum contiguous sum is "+
                                             maxSum);
        }
  }
