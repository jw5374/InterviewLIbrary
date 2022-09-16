
// return the sum of last digits in array A and modulo by 10^9 + 7
// do this recursively
public class LastDigitRecursiveSum {
    public static int lastSum(int N,int[] A)
    {
      if(N == 1) { 
        return A[N-1] % 10; 
      } 
      return ((A[N-1] % 10) + lastSum(N-1, A)) % 1000000007;
    } 
} 
