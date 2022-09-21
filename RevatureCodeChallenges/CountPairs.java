// count pairs in array A
// a pair is counted when all numbers between pair is less than the minimum of the paired numbers
// if there are no numbers between the pair, then it can be counted as a pair

/*
4
2 80 4 32
answer: 4

5  
10 3 4 8 6
answer: 6

2
2 4
answer: 1
*/

public class CountPairs {
  public static int countPairs(int N,int[] A)
  {
    int total = 0;
    for(int i = 0; i < A.length; i++) {
      int currMin;
      for(int j = i+1; j < A.length; j++) {
        total++;
        currMin = Math.min(A[i], A[j]);
        if(j == A.length - 1) {
          break;
        }
        if(currMin == A[j] && A[j] < A[j+1]) {
          continue;
        } else if(currMin == A[i] && A[j] < currMin) {
          continue;
        }
        break;
      }
    }
    return total;
  }
}
