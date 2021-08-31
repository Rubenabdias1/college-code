package murach.fv;



/* Name: Your name goes here
  * Class and Section: CS 166 01 or 02 (depending on your section)
  * Assignment: Program Assignment X (where X is the number of the assignment)
  * Due Date: The date the assignment is due to be turned in
  * Description: (for this example) This application displays some text on the console
  *    It can be used as a starting point for testing code
*/

	
	
	
	import java.util.Scanner;
	import java.text.NumberFormat;
	public class Stockfirm {
	
		public static void main(String [] args) {
			
			System.out.println("Welcome to the brokerage firm");
			System.out.println();
			
			double price=0;
			double total=0;
			
			
			String choice="yes";
			Scanner sc = new Scanner(System.in);
			
			
			while (choice.equalsIgnoreCase("yes")) {
				
				System.out.println("Please enter yout stock: \n");
				
				String stock = sc.nextLine();
				System.out.println("Please enter your quantity:  \n");
				int quantity=Integer.parseInt(sc.nextLine());
				if (stock.equalsIgnoreCase("coca cola")) {
					price=50;
												
				}
				else if (stock.equalsIgnoreCase("IBM")){
					price=80;
					
								
					
				}
				else if (stock.equalsIgnoreCase("Microsoft")){
					
					price=130;
					
					
				}
				else {
					System.out.println(" The stock you selected is not available \n Please enter your stock:\n ");
				}
				total =price*quantity;
				
				
				{
					// Format output
					System.out.println("Your total for the stocks you purchased:   \n"+ 
						NumberFormat.getCurrencyInstance().format(total));
					
					//Ask user to continue
					System.out.println("Do you want to continue y/n? ");
					choice=sc.nextLine();
					System.out.println();				
				}
							
			}
			System.out.println("Bye");
			sc.close();
		}

	}


