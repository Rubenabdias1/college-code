package exercises;

public class Employee implements Displayable, DepartmentsConstants {

    private int department;
    private String firstName;
    private String lastName;

    public Employee(int department, String lastName, String firstName) {
        this.department = department;
        this.lastName = lastName;
        this.firstName = firstName;
    }
    
    public String getDisplayText() {
    	return firstName + " " + lastName;
    }
    
    @Override
    public String toString() {
    	String text = "";
    	String dept = "";
    	
    	text += firstName +  " " + lastName;
    	
    	if (department == ADMIN) {
    		dept = "Administration";
    	}
    	else if (department == EDITORIAL) {
    		dept = "Editorial";
    	}
    	else if (department == MARKETING) {
    		dept = "Marketing";
    	}
    	
    	text += " (" + dept + ")";
    	
    	return text;
    }
}