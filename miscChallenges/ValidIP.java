import java.util.*;

public class ValidIP {
  	public static String  checkIPValidity(String addressIP)
	{
		String[] answer = addressIP.split("\\.");
		for(String num : answer) {
			int parsed = Integer.parseInt(num);
			if(parsed > 255 || parsed < 0) {
				return "INVALID";
			}
		}
		return "VALID";
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		
		// input for addressIP
		String addressIP = in.nextLine();
		in.close();
		String result = checkIPValidity(addressIP);
		System.out.print(result);
		
	}
}