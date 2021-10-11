package exam2;

/*
 * Name: Ruben Nunez
 * Assignment: Exam 2
 * Description: This program asks the user for an amount of cents and then distributes it in the amount of quarters,
 * 				dimes, nickels, and pennies that it can be distributed to.
 */

import java.util.Scanner;
public class ChangeCalculator {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String choice = "y";
		int centsAmount = 0;
		int rest;
		int quartersAmount = 0;
		int dimesAmount =  0;
		int nickelsAmount = 0;
		int penniesAmount = 0;
		
		System.out.println("Welcome to the Change Calculator");
		
		do {
			
			System.out.print("\nEnter number of cents: ");
			try {
				centsAmount = Integer.parseInt(sc.nextLine());
			} catch (NumberFormatException e) {
				System.out.println("Invalid input format. Please enter an integer");
				continue;
				
			}
			// rest variable will hold the reminding cents to distribute
			rest = centsAmount;
			quartersAmount = centsAmount / 25;
			rest = centsAmount % 25;
			dimesAmount =   rest / 10;
			rest = rest % 10;
			nickelsAmount = rest / 5;
			rest = rest % 5;
			penniesAmount = rest;


			String message = "Quarters: " + quartersAmount 
					 +"\n" + "Dimes: " + dimesAmount
					 +"\n" + "Nickels: " + nickelsAmount
					 +"\n" + "Pennies: " + penniesAmount;
			
			System.out.println(message);
			
			System.out.print("\nContinue? (y/n): ");
			choice = sc.nextLine();
			
		}
		while (choice.equalsIgnoreCase("y"));

		sc.close();
	}

}
