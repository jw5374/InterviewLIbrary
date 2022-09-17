import java.util.HashMap;


// given a coded system where letters a-z are mapped to numbers 0-25, and a digit string (e.g. "123")
// find the number of valid ways to decode string into letters
// for "123" :
// {1,2,3}, {12,3}, {1,23} are all valid ways to interpret the string thus you would return 3
public class DecodeWays {
    public static HashMap<String, Integer> memo = new HashMap<>();
	public static int validInterpretations(String decInput)
	{
		if(memo.get(decInput) != null) {
			return memo.get(decInput);
		}
		if(decInput.length() == 1) {
			return 1;
		}
		int answer = validInterpretations(decInput.substring(1));
        if(decInput.substring(0, 1).equals("0")) {
            memo.put(decInput, answer);
            return answer;
        }
		int parseTwo = Integer.parseInt(decInput.substring(0, 2));
		if(parseTwo <= 25 && parseTwo >= 0) {
			answer += validInterpretations(decInput.substring(2));
		}
		memo.put(decInput, answer);
		return answer;
	}

	public static void main(String[] args)
	{
		memo.put("", 1);
		String decInput = "123";
		int result = validInterpretations(decInput);
		System.out.print(result);
		
	}
}
