package exam1;

/*
 * Name: Ruben Nunez
 * Assignment: Exam 1
 * Description: This program tests the Grade class
 */

import java.util.Scanner;
import exam1.Grade;

public class GradeTest {

	public static void main(String[] args) {
		System.out.println("Welcome to the Letter Grade Converter");
		Scanner scanner = new Scanner(System.in);
		
		String prompt = "y";
		int number;
		String letterGrade = "F";
		
		// Testing constructor without a given number
		Grade grade = new Grade();
		System.out.println("\nGrade constructor when number not provided");
		System.out.println("Current grade: " + grade.getNumber());

		// Testing constructor with a given number
		grade = new Grade(70);
		System.out.println("\nCreating new Grade with 70");
		System.out.println("Current grade: " + grade.getNumber());
		
		while (prompt.equalsIgnoreCase("y")) {
			System.out.println("\nEnter numerical grade: ");
			number = scanner.nextInt();
			// Testing setter
			grade.setNumber(number);
			// Testing getter
			letterGrade = grade.getLetter(number);
			
			
			System.out.println("Letter grade: " + letterGrade);
			
			System.out.println("\nContinue? (y/n): ");
			scanner.nextLine();
			prompt = scanner.nextLine();
		}
		
		scanner.close();
		
		System.out.println("");
			

	}

}
