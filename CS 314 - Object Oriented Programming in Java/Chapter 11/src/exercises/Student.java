package exercises;

public abstract class Student {
	private String name;
	private String gender;
	
	public Student(String name, String gen) {
		this.name = name;
		this.gender = gen;
	}
	
	public abstract void study();
	
	public String toString() {
		return "name="+this.name+": Gender="+this.gender;
	}
	
	public void changeName(String newName) {
		this.name = newName;
	}

}
