package murach.fv;
import java.util.Scanner;
import java.text.NumberFormat;

public class StockBrocker {
	public static void main(String [] args) {
		
		System.out.println("Welocme to the brokerage firm");
		System.out.println();
		
		double price=0;
		double total=0;
		double totalStock=0;
		double subtotal=0;
		
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
			totalStock=totalStock+quantity;
			subtotal=subtotal+total;
			
			{
				// Format output
				System.out.println("Your total number of stocks you purchased:   "+ 
				totalStock+"\n"+ "Your bill: "+
						NumberFormat.getCurrencyInstance().format(total)+ "\n"+ "Subtotal:      "
				+ NumberFormat.getCurrencyInstance().format(subtotal));
				
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
