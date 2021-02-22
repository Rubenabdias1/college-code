package multiclass;

/*
 * Name: Ruben Nunez
 * Assignment: Chapter 4 Exercise 1
 * Description: Test program for the Triangle Class
 */
import java.util.Scanner;
import multiclass.Triangle;

public class TestTriangle {

	public static void main(String[] args) {

		System.out.println("Welcome to the Triangle Class Tester \n");
		
		Scanner sc = new Scanner(System.in);
		
		String choice = "y";
		
		while (choice.equalsIgnoreCase("y")) {
			System.out.println("Enter the width: ");
			double width = Double.parseDouble(sc.nextLine());
			
			System.out.println("Enter the length: ");
			double length = Double.parseDouble(sc.nextLine());
			
			Triangle t1 = new Triangle();
			
			t1.setWidth(width);
			t1.setLength(length);
			
			String message = "The width is:  " + t1.getWidth() + "\n" +
							 "The length is: " + t1.getLength()  + "\n" +
							 "The area is:   " + t1.getArea();
			
			System.out.println(message);
			System.out.println("Do you want to continue? (Y/n):\n");
			choice = sc.nextLine();
		}
		sc.close();
		
		
		
	}

}
