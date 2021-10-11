package ui;
// Using Grade class from Exam 1 (already tested when Exam 1)
public class StudentRecord {
	private Student student;
	private Grade[] quizes = {new Grade(0), new Grade(0)}; // two new quizzes grade
	private Grade midtermGrade = new Grade(0);
	private Grade finalGrade = new Grade(0);
	private Grade totalGrade = new Grade(0);
	
	public StudentRecord() {
		askName();
		askQuiz1(); 
		askQuiz2();
		askMidterm();
		askFinal();
	}
	
	// Getters and Setters
	
	public Student getStudent() {
		return student;
	}
	public void setStudent(Student student) {
		this.student = student;
	}
	
	public int getQuiz1 () {
		return quizes[0].getNumber(); // Grade class getNumber method
	}
	public void setQuiz1(int grade) {
		quizes[0].setNumber(grade);	// Grade class setNumber method
		computeTotalGrade();		// Letting the setters compute the total grade on every change
		
	}

	public int getQuiz2 () {
		return quizes[1].getNumber();
	}
	public void setQuiz2(int grade) {
		quizes[1].setNumber(grade);
		computeTotalGrade();  // same
		
	}
	
	public int getMidterm() {
		return midtermGrade.getNumber();
	}
	public void setMidterm(int grade) {
		midtermGrade.setNumber(grade);
		computeTotalGrade();
	}
	
	public int getFinal() {
		return finalGrade.getNumber();
	}
	public void setFinal(int grade) {
		finalGrade.setNumber(grade);
		computeTotalGrade();
	}
	
	public double computeQuizes() {
		double sumOfPercents = 0;
		
		for (Grade quizGrade: quizes) {
			int quizGradeNumber = quizGrade.getNumber();
			double quizPercent = ((double) quizGradeNumber) * 25.0 / 10.0; // had to cast or it would neglect decimal division
			sumOfPercents += quizPercent;
		}
		
		int amountOfQuizes = quizes.length;
		double quizesAverage = sumOfPercents / amountOfQuizes;
		return quizesAverage;
	}
	
	public void computeTotalGrade() {
		double quizesGrade = computeQuizes();
		double midtermGradeIn25 = ((double) midtermGrade.getNumber()) * 25.0 / 100.0;
		double finalGradeIn50 = ((double) finalGrade.getNumber()) * 50.0 / 100.0;
		totalGrade.setNumber(((int) (quizesGrade + midtermGradeIn25 + finalGradeIn50))); // cast again (not sure if should round)
	}
	
	
	public String buildName() {
		return "Name = " + student.getName();
	}
	public void printName() {
		Console.displayLine(buildName());
	}
	public void askName() {
		student = new Student();
		student.setName(Console.getString("What is the student's name? "));
	}
	
	
	public String buildQuiz1() {
		return "Quiz 1 score (out of 10 points) = " + getQuiz1();
	}
	public void printQuiz1() {
		Console.displayLine(buildQuiz1());
	}
	public void askQuiz1() {
		setQuiz1(Console.getInt("Quiz 1 score (out of 10 points)? "));
	}

	public String buildQuiz2() {
		return "Quiz 2 score (out of 10 points) = " + getQuiz2();
	}
	public void printQuiz2() {
		Console.displayLine(buildQuiz2());
	}
	public void askQuiz2() {
		setQuiz2(Console.getInt("Quiz 2 score (out of 10 points)? "));
	}

	public String buildMidterm() {
		return "Midterm score (out of 100 points) = " + getMidterm();
	}
	public void printMidterm() {
		Console.displayLine(buildMidterm());
	}
	public void askMidterm() {
		setMidterm(Console.getInt("Midterm score (out of 100 points)? "));
	}
	
	public String buildFinal() {
		return "Final exam score (out of 100 points) = " + getFinal();
	}
	public void printFinal() {
		Console.displayLine(buildFinal());
	}
	public void askFinal() {
		setFinal(Console.getInt("Final Exam score (out of 100 points)? "));
	}
	
	public String buildPercentGrade () {
		return student.getName() + "'s percent Grade is " + totalGrade.getNumber();
	}
	public void printPercentGrade() {
		Console.displayLine(buildPercentGrade());
	}
	
	public String buildLetterGrade () {
		return student.getName() + "'s letter Grade is " + totalGrade.getLetter();
	}
	public void printLetterGrade() {
		Console.displayLine(buildLetterGrade());
	}
	
	
	@Override
	public String toString() {
		String record = "";
		 record += buildName()
		 + "\n" + buildQuiz1()
		 + "\n" + "Quiz 1 score returned: " + getQuiz1()
		 + "\n" + buildQuiz2()
		 + "\n" + "Quiz 2 score returned: " + getQuiz2()
		 + "\n" + buildMidterm()
		 + "\n" + "Midterm score returned: " + getMidterm()
		 + "\n" + buildFinal()
		 + "\n" + "Final Exam score returned: " + getFinal()
		 + "\n" + "Letter grade = " + totalGrade.getLetter()
		 + "\n" + buildLetterGrade();
		 
				 
		 return record;
	}
}
