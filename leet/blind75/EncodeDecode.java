import java.util.*;
/*
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
FOUND ON LINTCODE (LEETCODE PREMIUM QUESTION)
JAVA VERSION for lintcode website

cannot submit to site without account unsure if complete solution
*/

public class EncodeDecode {
      /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public static String encode(List<String> strs) {
        StringBuffer sb = new StringBuffer();
        for(String s : strs) {
          sb.append(s.length());
          sb.append("=");
          sb.append(s);
        }
        return sb.toString();
    }

    /*
     * @param str: A string
     * @return: dcodes a single string to a list of strings
     */
    public static List<String> decode(String str) {
      List<String> decoded = new ArrayList<>();
      String[] split = str.split("");
      for(int i = 0; i < split.length; i++) {
        int j = i + 2;
        int length = Integer.parseInt(split[i]);
        String word = String.join("", Arrays.copyOfRange(split, j, j + length));
        if(split[i+1].equals("=")) {
          decoded.add(word);
          i += length + 1;
        }
      }
      return decoded;
    }
    
    public static void main(String[] args) {
      List<String> inputString = Arrays.asList("lint","code","love","you");
      String encoded = encode(inputString);
      List<String> decoded = decode(encoded);

      System.out.println(encoded);
      decoded.stream().forEach(System.out::print);
    }
}