import java.util.ArrayList;
import java.util.List;

// 41
// 27 30 4 22 20 29 1 25 37 29 8 13 3 21 5 38 27 38 3 5 14 5 9 25 30 32 24 18 36 18 10 30 5 33 19 16 10 32 36 8 24
// answer 3

// unsolved
public class SchoolTeams {
    public static int[] arr = { 27, 30, 4, 22, 20, 29, 1, 25, 37, 29, 8, 13, 3, 21, 5, 38, 27, 38, 3, 5, 14, 5, 9, 25, 30, 32, 24, 18, 36, 18, 10, 30, 5, 33, 19, 16, 10, 32, 36, 8, 24 };

    public static int[] simple = { 2, 1, 4, 3 };

    public static int find(int[] A, int val) {
        for(int i = 0; i < A.length; i++) {
            if(A[i] == val) {
                return i;
            }
        }
        return -1;
    }

    public static int schoolTeams(int N, int[] A)
    {
        int total = 0;
        List<Integer> teammembers = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            if(A[i] == -1) {
                continue;
            }
            if(!teammembers.contains(A[i])) {
                total++;
                teammembers.add(A[i]);
                int j = find(A, i+1);
                while((j != -1) && !teammembers.contains(A[j])) {
                    teammembers.add(A[j]);
                    A[j] = -1;
                    j = find(A, j+1);
                }
                A[i] = -1;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        System.out.println(schoolTeams(41, arr));
        // System.out.println(schoolTeams(4, simple));
    }
}
