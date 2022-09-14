// You are given a string S with words in camel case (actually titlecase, e.g. "HelloHowAreYouDoing")
// print all words in the order they appear in the string (each word gets its own line)

public class SplitCamelCasedString {
    public static void camelCase(String S) {
        String[] split = S.split("");
        int i = 0;
        while(i < split.length) {
            int j = i;
            while(j < split.length-1 && !split[j+1].equals(split[j+1].toUpperCase())) {
                j++;
            }
            if(j+1 >= split.length) {
                System.out.println(S.substring(i));
            } else {
                System.out.println(S.substring(i, j+1));
            }
            i = j+1;
        }
    }
    
}
