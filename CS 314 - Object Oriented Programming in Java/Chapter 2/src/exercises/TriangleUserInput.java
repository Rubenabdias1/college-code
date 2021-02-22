// TriangleUserInput.java

package exercises;

import java.util.Scanner;

/*
 * Name: Ruben Nunez
 * Assignment: Chapter 3 Exercise 1
 * Description: this program will compute the area of the triangle
 */

public class TriangleUserInput {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String choice = "yes";
		
		while(choice.equalsIgnoreCase("yes")) {
		
			System.out.println("Input the base of the triangle:");
			double base = scanner.nextDouble();
				
			System.out.println("Input the height of the triangle:");
			double height = scanner.nextDouble();
		
			scanner.close();
		
			double area= (base/2)*height;

			System.out.println();
	    
			System.out.println("Area of the Triangle");
			System.out.println("-------------------- \n");
			System.out.println("The base is:     " + base);
			System.out.println("The height is:   " + height);
			System.out.println("The area is:    " + area);

			System.out.println("Do you want to continue");
			choice = scanner.nextLine();
		}
		
		scanner.close();
		
	}

}
