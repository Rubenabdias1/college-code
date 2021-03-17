package exercises;

import java.util.Scanner;

// use integer division to divide time into hours and minutes?
public class TravelTimeApp {

    public static void main(String[] args) {
        // display a welcome message
        System.out.println("Welcome to the Travel Time Calculator");
        System.out.println();  // print a blank line

        // create the Scanner object
        Scanner sc = new Scanner(System.in);

        // perform invoice calculations until choice isn't equal to "y" or "Y"
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {
            // get input from the user
            System.out.print("Enter miles:           ");
            double miles = Double.parseDouble(sc.nextLine());
            System.out.print("Enter miles per hour:  ");
            double mph = Double.parseDouble(sc.nextLine());
            System.out.println();

            // calculate the travel time in hours with decimal division
            double hours = miles / mph;

            // get number of minutes as an int
            int minutes = (int) (hours * 60);

            // use integer arithmetic to get hours and minutes as int values
            int hoursInt = minutes / 60;
            minutes = minutes % 60;

            // display the result
            System.out.println("Estimated travel time");
            System.out.println("Hours:   " + hoursInt);
            System.out.println("Minutes: " + minutes);
            System.out.println();

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println();
        }
        sc.close();
    }
}