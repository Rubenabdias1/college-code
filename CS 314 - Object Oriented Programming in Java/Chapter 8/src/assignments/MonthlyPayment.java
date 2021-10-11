package assignments;

/*
 * Name: Ruben Nunez
 * Assignment: Assignment 5 Chapter 8
 * Description: This program calculates the monthly payment given a loan amount, yearly interest rate and number of years.
 */

import java.text.NumberFormat;
import assignments.Console;
public class MonthlyPayment {

	public static void main(String[] args) {
		
		System.out.println("Welcome to the Loan Calculator.");
		String choice = "y";
		double loanAmount;
		double yearlyInterestRate;
		int years;
		double monthlyPayment;
		String message;
		
		do {
			System.out.println("\nDATA ENTRY");
			loanAmount = Console.getDouble("Enter loan amount: ", 0.0, 1000000.0);
			yearlyInterestRate = Console.getDouble("Enter yearly interest rate: ", 0.0, 20.0) / 100;
			years = Console.getInt("Enter number of years: ", 0, 20);

			System.out.println("\nFORMATTED RESULTS");
			monthlyPayment = loanAmount * yearlyInterestRate / 12 /  (1 - 1/Math.pow(1 + yearlyInterestRate / 12, years * 12));
			message = "Loan amount:\t\t" + NumberFormat.getCurrencyInstance().format(loanAmount)  
			 + "\n" + "Yearly interest rate:\t" + NumberFormat.getPercentInstance().format(yearlyInterestRate)
			 + "\n" + "Number of Years:\t" + years
			 + "\n" + "Monthly payment:\t" + NumberFormat.getCurrencyInstance().format(monthlyPayment);
			System.out.println(message);
			System.out.println();
			
			choice = Console.getChoice("Continue? (y/n): ","y","n");
		}
		while (choice.equalsIgnoreCase("y"));
		
	}

	
	

}
