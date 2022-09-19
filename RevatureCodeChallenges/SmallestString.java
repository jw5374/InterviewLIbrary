import java.util.*;
// 42
// hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs

// swap characters until string S is lexicographically the smallest
// only able to swap if adjacent characters are not both vowels, or not both consonants
// can swap any number of times as long a condition hold true

// unsolved
public class SmallestString {
    public static List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');
    public static String smallestString(int N, String S)
    {
      String[] split = S.split("");
      for(int i = 0; i < N-1; i++) {
        char curr = S.charAt(i);
        char adj = S.charAt(i+1);
        if(!vowels.contains(adj) && !vowels.contains(curr)) {
          continue;
        }
        if(vowels.contains(adj) && vowels.contains(curr)) {
          continue;
        }
        if(curr < adj) {
          continue;
        }
        String temp = split[i];
        split[i] = split[i+1];
        split[i+1] = temp;
        S = String.join("", split);
        if(i != 0) {
          i -= 2;
        }
      }
      return String.join("", split);
    }

    public static void main(String[] args) {
      System.out.println(smallestString(42, "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"));
    }
}