package assignments;

/*
 * Name: Ruben Nunez
 * Assignment: Assignment 3
 * Description: This program displays customers data from a Customer database.
 */

import java.util.Scanner;
import assignments.CustomerDB;
import assignments.Customer;

public class CustomerTester {

	public static void main(String[] args) {
		System.out.println("Welcome to the Customer Viewer");
		
		Scanner sc = new Scanner(System.in);
		String choice = "y";
		int customerNumber;
		
		while (choice.equalsIgnoreCase("y")) {
			
			System.out.println("\nEnter a customer number: ");
			customerNumber = sc.nextInt();

			if(CustomerDB.customerExist(customerNumber)) {
				
				Customer customer = CustomerDB.getCustomer(customerNumber);
				System.out.println("\n" + customer.getNameAndAddress());
				
			} else {
				System.out.println("There is no customer number " + customerNumber + " in our records.");
			}
			
			
			System.out.println("\nDisplay another customer? (y/n):");
			sc.nextLine();
			choice = sc.nextLine();
		}
		
		sc.close();
		
	}

}
