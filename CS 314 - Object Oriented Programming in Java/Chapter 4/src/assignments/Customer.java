package assignments;

public class Customer {
	
	private String name;
	private String address;
	private String city;
	private String state;
	private String postalCode;


	public Customer(String name, String address, String city, String state, String postalCode) {
		this.name = name;
		this.address = address;
		this.city = city;
		this.state = state;
		this.postalCode = postalCode;
	}
	public Customer() {
		this.name = "";
		this.address = "";
		this.city = "";
		this.state = "";
		this.postalCode = "";
	}
	
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public String getAddress() {
		return this.address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	
	public String getCity() {
		return this.city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	
	public String getState() {
		return this.state;
	}
	public void setState(String state) {
		this.state = state;
	}
	
	public String getPostalCode() {
		return this.postalCode;
	}
	public void setPostalCode(String postalCode) {
		this.postalCode = postalCode;
	}
	
	public String getNameAndAddress() {
		return this.name + 
		"\n" + this.address + 
		"\n" + this.city + ", " + this.state + " " + this.postalCode;
	}
}
