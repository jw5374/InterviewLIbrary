import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PalindromicSubstrings {

    public static List<String[]> listPalindromicSubstrings(String s) {
        List<String[]> substrings = new ArrayList<>();
        String[] split = s.split("");
        for(int i = 0; i < split.length; i++) {
            int j = i;
            int k = i;
            while((j >= 0) && (k < split.length)) {
                if(split[j].equals(split[k])) {
                    substrings.add(Arrays.copyOfRange(split, j, k+1));
                    j--;
                    k++;
                } else {
                    break;
                }
            }
        }
        for(int i = 0; i < split.length; i++) {
            int j = i;
            int k = i+1;
            while((j >= 0) && (k < split.length)) {
                if(split[j].equals(split[k])) {
                    substrings.add(Arrays.copyOfRange(split, j, k+1));
                    j--;
                    k++;
                } else {
                    break;
                }
            }
        }
        return substrings;
    }

    public static int countPalindromicSubstrings(String s) {
        List<String[]> palindromicSubstrings = listPalindromicSubstrings(s);
        return palindromicSubstrings.size();
    }

    public static String[] longestPalindromicSubstring(String s) {
        List<String[]> substrings = listPalindromicSubstrings(s);
        String[] result = { "", "" };
        int max = 0;
        for(String[] sub : substrings) {
            if(sub.length >= max) {
                max = sub.length;
                result[1] = String.join("", sub);
            }
        }
        result[0] = max + "";
        return result;
    }

    public static void main(String[] args) {
        String test = "iewoslkdjfjkaioewurioewfjkdslkjdjkllkjjkfldsiowe";
        List<String[]> palinSubs = listPalindromicSubstrings(test); 
        String[] longestRes = longestPalindromicSubstring(test);
        System.out.println(countPalindromicSubstrings(test));
        for(String[] sub : palinSubs) {
            System.out.println(String.join("", sub));
        }
        System.out.println(longestRes[0] + " " + longestRes[1]);
    }
}
