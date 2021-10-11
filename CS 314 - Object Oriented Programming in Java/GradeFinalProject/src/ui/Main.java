package ui;
/*
 * Name: Ruben Nunez
 * Assignment: Final Project
 * Description: This program is a grading aid. It helps instructors grade two quizzes graded on the basis of 10 points,
 * a midterm exam and a final, each graded on the basis of 100 points. The program asks for input of each grade, then
 * displays the overall letter grade and the percent grade of the student. 
 */

public class Main {

	public static void main(String[] args) {
		StudentRecord record = new StudentRecord();
		Console.displayLine("= First Student=");
		record.printName();
		record.printQuiz1();
		record.printQuiz2();
		record.printMidterm();
		record.printFinal();
		record.printPercentGrade();
		Console.displayLine("======================================");
		System.out.println(record);
		String choice;
		do {
			Console.displayLine("======================================");
			record.askName();
			record.printName();
			
			record.printQuiz1();
			record.askQuiz1();
			record.printQuiz1();

			record.printQuiz2();
			record.askQuiz2();
			record.printQuiz2();
			
			record.printMidterm();
			record.askMidterm();
			record.printMidterm();

			record.printFinal();
			record.askFinal();
			record.printFinal();

			record.printPercentGrade();
			record.printLetterGrade();
			choice = Console.getChoice("Do again? (Y for Yes, or N for No)","y","n");
			
		} while (choice.equalsIgnoreCase("y"));

	}

}
