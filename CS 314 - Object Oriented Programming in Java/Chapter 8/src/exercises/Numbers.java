package exercises;

import java.util.Scanner;

public class Numbers {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String choice = "y";
		
		
		do {
			int number;
			System.out.println("Enter an integer: \n");
			
			try {
				number = Integer.parseInt(sc.nextLine());
			} catch (NumberFormatException e) {
				System.out.println("You entered the wrong format. Please enter an integer. \n");
				continue;
			}
			
			System.out.println("Number\tSquared\tCubed");
			System.out.println("======\t=======\t=====");
			
			for (int i = 1; i <= number; i++) {
				System.out.println(i + "\t" + i * i + "\t" + i*i*i );
			}
			
			
			System.out.println("Continue? (y/n)");
			choice = sc.nextLine();
			
		} while(choice.equalsIgnoreCase("y"));
		
		sc.close();

	}

}
