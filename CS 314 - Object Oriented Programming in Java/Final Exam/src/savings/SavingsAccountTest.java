package savings;
/*
 * Name: 		Ruben Nunez
 * Assignment: 	Final Exam
 * Description: This program will simulate a savings account. It asks the user for the starting balance, the amount deposited,
 * 				and the amount withdrawn. After that, it will print out the account statement. If the user decides to continue,
 * 				it will repeat the process adding up the balances each repetition. The statement will include every deposit
 * 				and withdrawal made to the account.
 */

public class SavingsAccountTest extends SavingsAccount {

	public static void main(String[] args) {
		String choice;
		do {
			balance = Console.getDouble("Enter the savings account's balance: ");
			deposit(Console.getDouble("Enter the amount deposited : "));
			withdraw(Console.getDouble("Enter the amount withdrawn : "));
			Console.displayLine();
			printAccount();
			
			choice = Console.getChoice("Do you want to continue: (y/n) ", "y", "n");
			
		} while(choice.equalsIgnoreCase("y"));
		
		Console.displayLine("Bye");

	}

}
