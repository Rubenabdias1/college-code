package exercises;

import java.util.Scanner;
import java.text.NumberFormat;

/*
 * Name: Ruben Nunez
 * Assignment: Chapter 3 Exercise 4
 * Description: This program sells stocks
 */


import java.util.Scanner;
import java.text.NumberFormat;

public class Stock {

	public static void main(String args[]) {
		
		System.out.println("Welcome to the brockerage frim");
		
		String choice = "yes";
		
		Scanner scanner = new Scanner(System.in);
		int price;
		
		
		while(choice.equalsIgnoreCase("yes")) {
			
			
			System.out.println("Please enter your stock: \n");
			
			String stock = scanner.nextLine();
			
			
			if (stock.equalsIgnoreCase("coca cola")) {
				price = 50;
				
			} 
			else if(stock.equalsIgnoreCase("IBM")) {
				price = 40;
				
			} 
			else if(stock.equalsIgnoreCase("Microsoft")) {
				price = 225;
				
			} 
			else {
				price = 0;
			}
			
			System.out.println("Input the quantity: ");
			int quantity = scanner.nextInt();
			
			int total = price * quantity;
			
			System.out.println("Your total for the stocks you pruchased: \n" 
			+ NumberFormat.getCurrencyInstance().format(total));
			
			System.out.println("Do you want to continue? (yes/no)\n");

			scanner.nextLine();
			choice = scanner.nextLine(); 
			System.out.println();
			
			
			
		}
		System.out.println("Bye!");
		scanner.close();
		
		
	}
}
