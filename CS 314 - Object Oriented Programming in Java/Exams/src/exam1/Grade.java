package exam1;

public class Grade {
	
	private int number;

	public Grade() {
		// Constructor when grade is not provided
		this.number = 0;
	}
	
	public Grade(int number) {
		// Constructor when grade is provided
		this.number = number;	
	}
	
	public void setNumber(int number) {
		// Setter for the grade number attribute
		this.number = number;
	}
	
	int getNumber() {
		// Getter for the grade number attribute
		return this.number;
		
	}
	
	String getLetter() {
		// Converts the stored grade number to a letter grade.
		int grade = this.number;
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
	
	String getLetter(int grade) {
		// Converts the provided grade number to a letter grade.
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
