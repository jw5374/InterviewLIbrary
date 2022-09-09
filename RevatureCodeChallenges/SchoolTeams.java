import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

// 41
// 27 30 4 22 20 29 1 25 37 29 8 13 3 21 5 38 27 38 3 5 14 5 9 25 30 32 24 18 36 18 10 30 5 33 19 16 10 32 36 8 24
// answer 3

public class SchoolTeams {
    public static int[] arr = { 27, 30, 4, 22, 20, 29, 1, 25, 37, 29, 8, 13, 3, 21, 5, 38, 27, 38, 3, 5, 14, 5, 9, 25, 30, 32, 24, 18, 36, 18, 10, 30, 5, 33, 19, 16, 10, 32, 36, 8, 24 };

    public static int[] simple = { 2, 1, 4, 3 };

    public static Map<Integer, Set<Integer>> teamgraph = new HashMap<>();

    public static Set<Integer> visitedMembers = new HashSet<>();

    public static void depthsearch(int value) {
        Set<Integer> edges = teamgraph.get(value);
        visitedMembers.add(value);
        if(edges == null) {
            return;
        }
        for(int i : edges) {
            if(!visitedMembers.contains(i)) {
                depthsearch(i);
            }
        }
    }

    public static int schoolTeams(int N, int[] A)
    {
        teamgraph.clear();
        visitedMembers.clear();
        int total = 0;
        for(int i = 0; i < N; i++) {
            if(teamgraph.get(A[i]) == null) {
                teamgraph.put(A[i], new HashSet<>());
                teamgraph.get(A[i]).add(i+1);
            } else {
                teamgraph.get(A[i]).add(i+1);
            }
            if(teamgraph.get(i+1) == null) {
                teamgraph.put(i+1, new HashSet<>());
                teamgraph.get(i+1).add(A[i]);
            } else {
                teamgraph.get(i+1).add(A[i]);
            }
        }

        for(int member : teamgraph.keySet()) {
            if(!visitedMembers.contains(member)) {
                depthsearch(member);
                total++;
            }
        }
        
        return total;
    }
    
    // for(Entry<Integer, Set<Integer>> entry : teamgraph.entrySet()) {
    //     System.out.print("key: " + entry.getKey() + "; ");
    //     for(int i : entry.getValue()) {
    //         System.out.print("value: " + i + "; ");
    //     }
    //     System.out.println();
    // }
    
    public static void main(String[] args) {
        System.out.println(schoolTeams(arr.length, arr));
        System.out.println(schoolTeams(4, simple));
    }
}
