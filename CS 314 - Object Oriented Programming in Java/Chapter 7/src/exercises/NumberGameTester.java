package exercises;
import java.util.Scanner;

public class NumberGameTester {

	public static void main(String[] args) {
		System.out.println("Welcome to the Number Guessing Game");
		System.out.println();

		Scanner sc = new Scanner(System.in);
		NumberGame game = new NumberGame();
		System.out.println("I have selected a number between 0 and " + game.getUpperLimit());

		int guess = 51;
		int number = game.getNumber(); // calling it once
		
		while (guess != number) {
			System.out.print("Enter your guess: ");
			guess = Integer.parseInt(sc.nextLine());
			
			if (guess < number) {
				System.out.println("Your guess is too low.\n");
			} else {
				System.out.println("Your guess is too high.\n");
			}
			
			game.incrementGuessCount();
			
		}
		System.out.println("Correct!\n");
		
		System.out.println("You guessed the correct number in " + game.getGuessCount() + " times\n");
		
		sc.close();
	}

}
