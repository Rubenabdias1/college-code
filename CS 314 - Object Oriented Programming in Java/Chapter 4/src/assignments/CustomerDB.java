package assignments;

import assignments.Customer;

public class CustomerDB {
	
	
	static Customer getCustomer(int customerNumber) {
		
		if(customerNumber == 1001) {
			return new Customer("Barbara White", "3400 Richmond Parkway #3423", "Bristol", "CT", "06010");
		} 
		else if(customerNumber == 1002) {
			return new Customer("Karl Vang", "327 Franklin Street", "Edina", "MN", "55435");
		}
		else if(customerNumber == 1003) {
			return new Customer("Ronda Chavan", "518 Commanche Dr.", "Greensboro", "NC", "27410");
		}
		
		return new Customer();
		
	}
	
	static boolean customerExist(int customerNumber) {
		return (customerNumber == 1001) || (customerNumber == 1002) || (customerNumber == 1003);
	}

}
