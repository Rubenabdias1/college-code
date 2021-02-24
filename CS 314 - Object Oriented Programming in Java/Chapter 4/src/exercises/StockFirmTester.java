package exercises;

import exercises.StockFirmMethods;

public class StockFirmTester {

	public static void main(String[] args) {
		System.out.println("Welcome to the brockrage firm\n");
		
		StockFirmMethods sample = new StockFirmMethods();
		
		String message = "Stock:    " + sample.getStock() + "\n" 
					   + "Quantity: " + sample.getQuantity() + "\n"
					   + "Price:    " + sample.getPrice() + "\n"
					   + "Total:    " + sample.getTotalformatted() + "\n";
		
		System.out.println(message);
		
		System.out.println("This is after we set the values");
		
		sample.setStock("IBM");
		sample.setQuantity(7);
		sample.setPrice(90);
		sample.ComputeTotal();
		
		message = "Stock:    " + sample.getStock() + "\n" 
				+ "Quantity: " + sample.getQuantity() + "\n"
				+ "Price:    " + sample.getPrice() + "\n"
				+ "Total:    " + sample.getTotalformatted() + "\n";
		
		System.out.println(message);
		
		sample = new StockFirmMethods("IBM", 988.0, 7);
		message = "Stock:    " + sample.getStock() + "\n" 
				+ "Quantity: " + sample.getQuantity() + "\n"
				+ "Price:    " + sample.getPrice() + "\n"
				+ "Total:    " + sample.getTotalformatted() + "\n";
		
		System.out.println(message);
		

	}

}
