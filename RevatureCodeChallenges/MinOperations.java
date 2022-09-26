// given array A, split array into 2 equal parts with both equal sum and element count
// you can do so by taking any index i, and adding value v
// v must be positive
// output:
// first line is number of operations to make equal
// followed by all operations used to make equal
// minimize the number of operations required

public class MinOperations {
  public static void minOperations(int N, int[]A)
  {
    int[] first = Arrays.copyOfRange(A, 0, (N/2));
    int[] second = Arrays.copyOfRange(A, N/2, N);
    int diff = IntStream.of(first).sum() - IntStream.of(second).sum();
    if(N == 1) {
      System.out.println("1");
      System.out.println(Math.abs(diff) + " 2");
      return;
    }
    if(N%2 != 0) {
      if(diff < 0) {
        System.out.println("1");
        System.out.println(Math.abs(diff) + " 1");
      } else {
        System.out.println("1");
        System.out.println(Math.abs(diff) + " " + N+1);
      }
      return;
    }
    if(diff < 0) {
      System.out.println("2");
      System.out.println(Math.abs(diff) + " 1");
      System.out.println("0 " + (N+2));
    } else {
      System.out.println("2");
      System.out.println("0 1");
      System.out.println(Math.abs(diff) + " " + (N+2));
    }
  } 
}
