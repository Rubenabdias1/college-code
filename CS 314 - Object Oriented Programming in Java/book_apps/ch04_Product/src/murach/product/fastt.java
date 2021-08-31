package murach.product;

import java.util.Scanner;
import java.text.NumberFormat;

public class fastt 
{

	public static void main(String[] args) 
	{
		String continuePrompt, message;
		double price = 0, chickenPrice = 5.00, fishPrice = 9.00, burgerPrice = 9.00, total = 0;
		double chickenTotal = 0, fishTotal = 0, burgerTotal = 0;
		// Creates an object named "fastFoodObject" of the "fastFood" Class to be used when calling methods
		//fastFood fastFoodObject = new fastFood();
		
		//fastFoodObject = fastFood.setPrice(chickenPrice);
		
		// Creates userInput as an object of the scanner Class
		Scanner userInput = new Scanner(System.in);
		Scanner userQuantity = new Scanner(System.in);
        System.out.println("Welcome to the Fast Food Order Menu");
        message = "Chicken $5.00" + "\n" + "Fish $9.00"  + "\n" + "Burger $9.00" +"\n";
        System.out.println(message);
        
        continuePrompt = "y";
        while (continuePrompt.equalsIgnoreCase("y"))
        {
			System.out.println("Please make a selection: ");
			// Calls the "useRInput" object and stores it's value into "foodChoice"
			// nextLine() Advances the scanner object to the end of the line, then returns the completed sentence. Also advances to the next
			// line in the program.
			// next() Returns the first complete token AKA a single word. Reads each word delimited by spaces, and prints out each word separately. 
        	String foodChoice = userInput.nextLine();
        	//fastFoodObject = fastFood.getChoice(foodChoice);
        	
        	//System.out.println("Enter quantity: ")
        	// Assigns a user entered number "userQuantity" to the variable "quantityAmt"
        	//String quantityAmt = userQuantity.nextLine();
        	// Changes "quantityAmt" from a String to an int
        	//int quantity = Integer.parseInt(quantityAmt);
        	
        	
        	
        	if (foodChoice.equalsIgnoreCase("chicken"))
        	{
            	System.out.println("Enter quantity: ");
            	// Assigns a user entered number "userQuantity" to the variable "quantityAmt"
            	String quantityAmt = userQuantity.nextLine();
            	// Changes "quantityAmt" from a String to an int
            	int quantity = Integer.parseInt(quantityAmt);
            	
        		chickenTotal = chickenPrice * quantity;
            	total = chickenTotal + fishTotal + burgerTotal;
            	
            	System.out.println(foodChoice);
            	System.out.println("Your order " + NumberFormat.getCurrencyInstance().format(chickenTotal));
            	System.out.println("Your subtotal " + NumberFormat.getCurrencyInstance().format(total));
            	System.out.println("Continue? Y/N?");
            	
            	// sets the continuePrompt variable equal to the users input
            	continuePrompt = userInput.nextLine();
        	}
        	else if (foodChoice.equalsIgnoreCase("Fish"))
        	{
            	System.out.println("Enter quantity: ");
            	// Assigns a user entered number "userQuantity" to the variable "quantityAmt"
            	String quantityAmt = userQuantity.nextLine();
            	// Changes "quantityAmt" from a String to an int
            	int quantity = Integer.parseInt(quantityAmt);
            	
        		fishTotal = fishPrice  * quantity;
            	total = chickenTotal + fishTotal + burgerTotal;
            	
            	System.out.println(foodChoice);
            	System.out.println("Your order " + NumberFormat.getCurrencyInstance().format(fishTotal));
            	System.out.println("Your subtotal " + NumberFormat.getCurrencyInstance().format(total));
            	System.out.println("Continue? Y/N?");
            	
            	// sets the continuePrompt variable equal to the users input
            	continuePrompt = userInput.nextLine();
        	}
        	else if (foodChoice.equalsIgnoreCase("Burger"))
        	{
            	System.out.println("Enter quantity: ");
            	// Assigns a user entered number "userQuantity" to the variable "quantityAmt"
            	String quantityAmt = userQuantity.nextLine();
            	// Changes "quantityAmt" from a String to an int
            	int quantity = Integer.parseInt(quantityAmt);
            	
        		burgerTotal = burgerPrice  * quantity;
            	total = chickenTotal + fishTotal + burgerTotal;
            	
            	System.out.println(foodChoice);
            	System.out.println("Your order " + NumberFormat.getCurrencyInstance().format(burgerTotal));
            	System.out.println("Your subtotal " + NumberFormat.getCurrencyInstance().format(total));
            	System.out.println("Continue? Y/N?");
            	
            	// sets the continuePrompt variable equal to the users inputasd
            	continuePrompt = userInput.nextLine();
        	}
        	else
        	{
        		System.out.println("Error! Please enter a valid choice.");
            	System.out.println("Your order 0.00");
            	System.out.println("Your subtotal " + NumberFormat.getCurrencyInstance().format(total));
            	System.out.println("Continue? Y/N?");
            	
            	// sets the continuePrompt variable equal to the users input
            	continuePrompt = userInput.nextLine();
        	}

        }
        // Closes the userInput object to save memory
        userInput.close();
        userQuantity.close();
	}
}
