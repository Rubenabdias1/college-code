package quiz1;
import java.util.Scanner;
/*
 * Name: Ruben Nunez
 * Assignment: Quiz 1
 * Description: This program prints the letter grade from a numeric grade
 */

public class quiz1 {

	public static void main(String[] args) {
		System.out.println("Welcome to the Letter Grade Converter");
		Scanner scanner = new Scanner(System.in);
		
		String prompt = "y";
		int grade;
		String letterGrade = "F";
		
		while (prompt.equalsIgnoreCase("y")) {
			System.out.println("\nEnter numerical grade: ");
			grade = scanner.nextInt();
			
			if( grade >= 88 ) {
				letterGrade = "A";
			} 
			else if(grade >= 80) {
				letterGrade = "B";
			}
			else if(grade > 67) {
				letterGrade = "C";
			}
			else if(grade >= 60) {
				letterGrade = "D";
			}
			
			System.out.println("Letter grade: " + letterGrade);
			
			System.out.println("\nContinue? (y/n): ");
			scanner.nextLine();
			prompt = scanner.nextLine();
		}
		
		scanner.close();
		
		System.out.println("");
			
		

	}

}
