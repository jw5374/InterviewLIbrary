import java.text.DecimalFormat;
import java.util.Arrays;

// find average of values in array A after removing highest and lowest values
// must format to 5 decimal places
public class AverageCoin {
    public static String averageValue(int N,int[] A)
    {
      Arrays.sort(A);
      double avg = 0;
      DecimalFormat df = new DecimalFormat("#.00000");
      for(int i = 1; i < A.length-1; i++) {
        avg += A[i];
      }
      return df.format((avg / (A.length-2)));
    }
}
