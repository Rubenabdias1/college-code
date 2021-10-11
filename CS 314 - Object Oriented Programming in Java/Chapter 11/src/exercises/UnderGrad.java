package exercises;

public class UnderGrad extends Student {
	
	private String codeID="U";
	
	public UnderGrad (String name, String id, String gen) {
		super(name, gen);
		this.codeID = id;
	}
	
	
	@Override
	public void study() {
		if (codeID.equalsIgnoreCase("g")) {
			System.out.println("Student is graduate ");
		} 
		else if (codeID.equalsIgnoreCase("u")) {
			System.out.println("Student is undergraduate");
		}
	}
	
	public static void main(String[] args) {
		
		Student student1 = new UnderGrad("Ruben Nunez", "485641", "male");
		
	}
}
