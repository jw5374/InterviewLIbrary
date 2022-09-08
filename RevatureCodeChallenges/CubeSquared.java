
public class CubeSquared {
    public static void cubeSquare(int T,int[] N){
        for(int i = 0; i < T; i++) {
            int total = 0;
            for(int j = 1; j <= N[i]; j++) {
                int sqrt = (int) Math.floor(Math.sqrt(j));
                int cbrt = (int) Math.floor(Math.cbrt(j));
                if((sqrt * sqrt) == j) {
                    total++;
                    continue;
                }
                if((cbrt * cbrt * cbrt) == j) {
                    total++;
                    continue;
                }
            }
            System.out.println(total);
        }
    }
}
