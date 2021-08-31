package exercises;

public class Candy {

	public static void main(String[] args) {
		int age=50;
		int weight=220;
		int height=72;
		
		System.out.println("This program will calculate the number of 230 calorie");
		System.out.println("candy bars to eat and mantain your weight.\n");
		
		double caloriesMale, caloriesFemale;
		
		caloriesMale = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age);
		caloriesFemale = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age);
		
		System.out.println("A female with those measurements should eat " + (caloriesFemale / 230)  + " candy bars per day to maintain her weight.");
		System.out.println("A male with those measurements should eat " + (caloriesMale / 230)  + " candy bars per day to maintain his weight.");
		

	}

}
