package bonus;

import java.util.Arrays;

public class RandomLetterGrades {
	
	public static void main (String[] args) {
        int[] randomGrades = new int[100];

        System.out.println( "The size of the array is: " + randomGrades.length);
        
        for (int i=0; i < randomGrades.length; i++) {
            randomGrades[i] = (int)(Math.random() * 100);
        }

        
        System.out.println("Print all the elements of the array:");

        for (int grade: randomGrades) {
            System.out.println(grade);
        }
        
        Arrays.sort(randomGrades);
        System.out.println();

        for (int grade: randomGrades) {
            System.out.println("The grade is: " + grade + " The letter is: " + getLetter(grade));
        }
        
    }

    public static String getLetter(int grade) {
		// Converts the grade number to a letter grade.
		
		if( grade >= 88 ) {
			return "A";
		} 
		else if(grade >= 80) {
			return "B";
		}
		else if(grade > 67) {
			return "C";
		}
		else if(grade >= 60) {
			return"D";
		}
		
		return "F";
	}
    
}