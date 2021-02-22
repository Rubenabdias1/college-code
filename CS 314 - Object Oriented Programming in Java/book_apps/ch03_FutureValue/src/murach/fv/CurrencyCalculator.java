package murach.fv;
import java.util.Scanner;
import java.text.NumberFormat;

/*
 * Name:
 * Course:
 * Section:
 * Assignment: 
 * 
 * This program will convert currency between Dollar and Euro based on the example
 * in the book
 * 
 */
public class CurrencyCalculator {

	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
		
		// Request input from users using the Scanner class
		Scanner sc=new Scanner(System.in);  // declare the Scanner object "sc" 
		
		String choice="yes";  //Declare String variable 
		
		 
		while(choice.equalsIgnoreCase("yes")){
			
			System.out.println("Enter your Money value:  ");// Request input from user 
			double value1 = Double.parseDouble(sc.nextLine());// Convert String to double using "Double"
			//class and parseDouble method
			System.out.println("Enter your currency type:    "); // 
			String currency= sc.nextLine(); //Declare String "Currency"
			double value2=0; // This what the program will compute
			
			if (currency.equalsIgnoreCase("USD")) // If statement to compare string "USD" 
			
			{ 
				value2=value1*0.734; // If the user input USD it will convert it to EURO
			} // close the first if statement
			else if(currency.equalsIgnoreCase("EURO"))// if statement for another condition when user input "EURO" 
			
			{
				
			value2=value1*1.34;  // convert from EURO to dollar
			
			}
			else  {
				System.out.println("Conversion rate: 1 USD = 0.734 EUR \n" +"Conversion rate: 1 EUR=1.34 USD ");
				
			}
			
			// Format the output
			
			 System.out.println("Currency Value:               " + 
	                    NumberFormat.getCurrencyInstance().format(value2)); // chaining method 
			 	            System.out.println();
			 	            
			 	            // Ask the user to continue or terminate
			 	           System.out.print("Continue? (y/n): ");
			 	            choice = sc.nextLine();
			 	            System.out.println();
			 	           
			}
		 System.out.println("bye");
		sc.close();
		}

	}


