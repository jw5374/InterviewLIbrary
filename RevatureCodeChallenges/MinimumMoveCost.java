// move the given index of array to the end of the array by swapping adjacent elements
// each move has a cost
// cost is the difference between target and element to be moved

public class MinimumMoveCost {
    public static int findMin(int N,int[] A, int index)
    {
      int cost = 0;
      for(int i = index-1; i < N-1; i++) {
        int temp = A[i+1];
        if(temp > A[i]) {
          cost += temp - A[i];
        }
        A[i+1] = A[i];
        A[i] = temp;
      }
      return cost;
    }
}