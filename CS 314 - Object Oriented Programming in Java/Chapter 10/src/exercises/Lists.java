package exercises;

public class Arrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		final int titlecount = 100;
		double [] prices = new double[4];
		
		String titles [] = new String[titlecount];
		
		prices[0] = 14.95;
		prices[1] = 15.95;
		prices[2] = 16.95;
		prices[3] = 17.95;
		
		titles[0] = "java";
		titles[1] = "C#";
		titles[2] = "C++";
		
		double items [] = {14.95,15.95,16.95};
		
		int[] values = new int[10];
		
		for (int i = 0; i < values.length; i++) {
			values[i] = i;
		}

		System.out.println("Print the elements of the array: \n");
		for (int i = 0; i < prices.length; i++) {
			System.out.println(prices[i]);
		}

		int sum = 0;
		for (int i = 0; i < prices.length; i++) {
			sum += prices[i];
		}
		double average = sum/prices.length;
		System.out.println("The sum is:\t"+ sum);
		System.out.println("The average is:\t"+ average);
		
		
	}	
	

}
