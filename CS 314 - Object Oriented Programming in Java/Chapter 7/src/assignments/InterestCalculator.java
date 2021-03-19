package assignments;

/*
 * Name: Ruben Nunez
 * Assignment: Assignment 4 Chapter 7
 * Description: This program prompts the user for a loan and an interest rate then displays the interest.
 */

import java.text.NumberFormat;
import java.util.Scanner;
import java.math.BigDecimal; 

public class InterestCalculator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Welcome to the Interest Calculator");
		
		Scanner sc = new Scanner(System.in);
		String choice = "y";
		BigDecimal loan;
		BigDecimal interestRate;
		BigDecimal interest;
		
		do {
			// Input
			System.out.println("\nEnter loan amount: ");
			try {
				loan = new BigDecimal(sc.nextLine());
			} catch (NumberFormatException e) {
				System.out.println("You entered the wrong format. Please enter an integer. \n");
				continue;
			}
			
			System.out.println("Enter interest rate: ");
			try {
				interestRate = new BigDecimal(sc.nextLine());
			} catch (NumberFormatException e) {
				System.out.println("You entered the wrong format. Please enter a decimal number. \n");
				continue;
			}
			
			// Processing
			interest = loan.multiply(interestRate);
			
			// Output
			System.out.println("\nLoan amount:\t\t"+NumberFormat.getCurrencyInstance().format(loan));
			System.out.println("Interest rate:\t\t"+NumberFormat.getPercentInstance().format(interestRate));
			System.out.println("Interest:\t\t"+NumberFormat.getCurrencyInstance().format(interest));
			
			System.out.println("\nContinue? (y/n): ");
			choice = sc.nextLine();
		} while (choice.equalsIgnoreCase("y"));
		
		sc.close();
	}

}
