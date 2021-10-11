package exercises;


import java.util.Arrays;
public class Lists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
final int titlecount=100;
		double prices [] =new double [4];
		String titles []=new String[titlecount];
		
		prices [0]=14.95;
		prices [1]=15.95;
		prices [2]=16.95;
		prices [3]=17.95;
		//prices [4]=18.95;
		
		titles [0]="Java";
		titles [1]="C#";
		titles [2]="C++";
		
		// Creating an array and assign values in one statement
		
		double items []= {15.95,16.95,17.95};
		
		System.out.println("prices: \n"+prices.length);
		System.out.println("titles:  \n"+ titles.length);
		System.out.println("titles:  \n"+items.length);
		
		// Code that prints an array of prices to the console
		
		System.out.println("Print the elements in prices: \n");
		for (int i=0; i<prices.length; i++) {
			System.out.println(prices[i]);
		}
		
		// Code that computes the average of the array of prices
		
		System.out.println("This is the average of array prices: \n ");
		double sum=0.0;
		for (int i=0; i<prices.length; i++) {
			sum+=prices[i];
			
		}
		double average=sum/prices.length;
		System.out.println("The sum is: "+sum);
		System.out.println("The average is:  "+average);
		System.out.println();
		
		// Code to print the element of the array using the enhanced for loop
		
		System.out.println("This is using the enhanced for loop \n");
		
		for(double theprices: prices) {
			System.out.println(theprices);
			System.out.println("");
			
		}
			
		// Code that computes the average of the array using the enhanced loop 
		double sum2=0.0;
		for (double enhancedloop:prices) {
			
			sum2+=enhancedloop;
		}
		
		double average2=sum2/prices.length;
		System.out.println("The average using the enhanced loop:  "+average2);
		
		System.out.println("==================================================\n");
			
		// Rectangular array 
		
		int RectangularArray [][]= new int [3][2];
		RectangularArray[0][0]=1;
		RectangularArray[0][1]=2;
		RectangularArray[1][0]=3;
		RectangularArray[1][1]=4;
		RectangularArray[2][0]=5;
		RectangularArray[2][1]=6;
		
		int RectangularArray2 [][]= {{1,2}, {3,4}, {5,6}};
		
		
		// How to use nested for loops to process a rectangular array
		
					
		
		
		for (int[] row : RectangularArray)
		{
		    if (row != null)
		        for (int col : row)
		            System.out.print(col + " ");
		 
		    System.out.println();
		}
		System.out.println("=================================\n");
		
		// Java Arrays class 
		
		
		int numbers [] =new int[5];
		Arrays.fill(numbers, 1);
		//=============================
		
		int [] numbers2= {1,6,8,4,5,9};
		Arrays.sort(numbers2);
		
		for (int number: numbers2) {
			
			System.out.println(number+"");
					
						
		}
		
		System.out.println("====================================\n");
		
		// How to search an array
		int index =Arrays.binarySearch(numbers2, 5);
		System.out.println("Number 5 is located at index: "+ index);
		System.out.println();
		
		System.out.println("====================================\n");
		
		// How to create a reference to an array
		
		double grades []= {99.3, 88.0, 95.2, 60.0};
		double percentages []=grades;
		percentages [1]=70;
		
		System.out.println("grades[1] =: "+grades[1]);
		System.out.println("====================================\n");
		
		// How to create a shallow copy of an array
		double percentages2 []= Arrays.copyOf(grades, grades.length);
		percentages2 [1]=99;
		
		System.out.println("percentages2[1] =: "+percentages2[1]);
		
		System.out.println("grades[1] =: "+grades[1]);
		
	}

}
