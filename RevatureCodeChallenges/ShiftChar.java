// Shift a given character A by K places
// if A becomes greater than 'Z' then loop back around 

public class ShiftChar {
    public static char rightShift(char A, int K)
    {
      if(A+K > 90) {
        return (char)(65 + ((K-1) % 26));
      }
      return (char)(A + K);
    }
    
}
