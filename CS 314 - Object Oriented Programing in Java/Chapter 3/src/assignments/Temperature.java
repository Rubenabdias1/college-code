package assignments;
import java.util.Scanner;
/*
 * Name: Ruben Nunez
 * Assignment: Project 3-2: Convert temperature
 * Description: This program prompts the user for a temperature in Fahrenheit
 * 				and a weight in kilograms. Then, it converts the temperature
 * 				to Celsius and the weight to Pounds.
 */
public class Temperature {

	public static void main(String[] args) {
		System.out.println("Welcome to the Temperature and Weights Converter\n");
		
		Scanner sc = new Scanner(System.in);

		String choice = "y";
		double fahrenheits;
		double weight;
		double degreesInCelcius;
		double weightInPounds;

		while (choice.equalsIgnoreCase("y")) {
			
			System.out.println("Enter degrees in Fahrenheit: ");
			fahrenheits = sc.nextDouble();
			System.out.println("Enter weights in kilograms: ");
			weight = sc.nextDouble();

			degreesInCelcius = (fahrenheits - 32) * 5/9;
			weightInPounds =  weight / 0.453592; 

			System.out.println("Degrees in Celsius: " + degreesInCelcius);
			System.out.println("Weights in Pound: " + weightInPounds);

			System.out.println("\nContinue? (y/n): ");
			choice = sc.nextLine();
			sc.nextLine();
		}
		
		sc.close();
		

	}

}
