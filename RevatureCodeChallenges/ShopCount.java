import java.util.HashSet;
import java.util.Set;

// infinite photcopy shops have confidential document
// array is in binary tree form
// each shop can either give documents to children or not
// children are: shopId * 2, and (shopId *2) + 1
public class ShopCount {
    public static int totalShops(int N, int[] A) {
        Set<Integer> allShops = new HashSet<>();
        for(int i : A) {
            int parent = i / 2;
            do {
                allShops.add(parent);
                allShops.add(parent * 2);
                allShops.add((parent * 2) + 1);
                parent /= 2;
            } while(parent > 0);
        }
        return allShops.size();
    }
}
