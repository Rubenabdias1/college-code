package exercises;

import java.util.Scanner;

public class DaysOfTheWeek {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String choice = "y";
		
		do {
			int number;
			System.out.println("Enter the number of days between 1 and 7: \n");
			
			try {
				number = Integer.parseInt(sc.nextLine());
			} catch (NumberFormatException e) {
				System.out.println("You entered the wrong format. Please enter an integer. \n");
				continue;
			}
			switch(number) {
			case 1:
				printDay(number, "Monday");
				break;
			case 2:
				printDay(number, "Tuesday");
				break;
			case 3:
				printDay(number, "Wednesday");
				break;
			case 4:
				printDay(number, "Thursday");
				break;
			case 5:
				printDay(number, "Friday");
				break;
			case 6:
				printDay(number, "Saturday");
				break;
			case 7:
				printDay(number, "Sunday");
				break;
			default:
				System.out.println("Invalid day number.");
			
			
			System.out.println("Do you wish to continue? (y/n)");
			choice = sc.nextLine();
			}
		} while(choice.equalsIgnoreCase("y"));
		
		sc.close();

	}
	
	public static void printDay(int number, String day) {
		System.out.println("You entered " + number + ". The day of the week is " + day + ".");
		
	}
}
