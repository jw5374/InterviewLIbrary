// rotate matrix 90 degrees to the right
public class RotateMatrix {
 	public static int[][] transpose(int[][] mat) {
		int[][] transposed = new int[mat[0].length][mat.length];
		for(int i = 0; i < mat.length; i++) {
			for(int j = 0; j < mat[0].length; j++) {
				transposed[i][j] = mat[j][i];
			}
		}
		return transposed;
	}
	public static int[][] rotatedImage(int[][] matrix)
	{
		int[][]  answer = new int[matrix.length][matrix[0].length];
		int j = 0;
		for(int i = matrix.length - 1; i >= 0; i--) {
			answer[j] = matrix[i];
			j++;
		}
		answer = transpose(answer);
		
		return answer;
	} 
}