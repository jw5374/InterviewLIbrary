import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class EqualSplit {
    public static int equalSplitArray(int N,int[] A)
    {
      Set<Integer> firstHalf;
      Set<Integer> secondHalf;
      for(int i = 0; i < N; i++) {
        int[] first = Arrays.copyOfRange(A, 0, i);
        int[] second = Arrays.copyOfRange(A, i, N);
        firstHalf = Arrays.stream(first).boxed().collect(Collectors.toSet());
        secondHalf = Arrays.stream(second).boxed().collect(Collectors.toSet());
        if(firstHalf.size() == secondHalf.size()) {
          return i;
        }
      }
      return -1;
    }
}
