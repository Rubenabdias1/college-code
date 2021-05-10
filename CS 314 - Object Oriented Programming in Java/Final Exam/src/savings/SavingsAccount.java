package savings;
import java.text.NumberFormat;

public class SavingsAccount {
	static double balance;            // Starting balance
	static double deposits;           // Amount of deposits for a month
	static double withdrawn;          // Amount withdrawn in a month
	static double totalDeposits = 0;  // Deposit accumulator
	static double totalWithdrawn = 0; // Withdrawal accumulator
	static double endingBalance=0;   // Ending balance
	
	static double withdraw(double amount) {
		totalWithdrawn += amount;
		withdrawn += amount;
		balance -= amount;
		return balance;
	}
	
	static double deposit(double amount) {
		deposits += amount;
		totalDeposits += amount;
		balance += amount;
		return balance;
	}

	static double getBalance() {
		endingBalance += balance;
		withdrawn = 0;  // Reset
		deposits = 0;	// Reset
		balance = 0;	// Reset
		return endingBalance;
	}
	
	static void printAccount() {
		NumberFormat currency = NumberFormat.getCurrencyInstance();
		String message = "";
		message += "Total deposited:  " + currency.format(totalDeposits)
		 + "\n" +  "Total withdrawn:  " + currency.format(totalWithdrawn)
		 + "\n" +  "Ending balance:   " + currency.format(getBalance());

		Console.displayLine(message);
	}

}
