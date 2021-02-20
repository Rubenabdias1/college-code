package murach.product;

import java.text.NumberFormat;

public class FastFoodclass {
	
	// the instance variables
	private String choice;
	private double subtotal;
	private double total;
	private double price;
	
	// the constructor
	public FastFoodclass(String choice, double total, double price, double subtotal) {
		this.choice = choice;
		this.subtotal = subtotal;
		this.total =total;
		this.price = price;
	}
	
	// the set and get methods
	public void setChoice(String choice) {
		this.choice = choice;
	}
	
	public String getChoice() {
		return choice;
	}
	
	public void setSubtotal(double subtotal) {
		this.subtotal = subtotal;
	}
	
	public double getSubtotal() {
		return subtotal;
	}
	
	public void setTotal(double total) {
		this.total = total;
	}
	
	public double getTotal() {
		return total;
	}
	
	public void setPrice(double price) {
		this.price = price;
	}
	
	public double getPrice() {
		return price;
	}
	public double computetotal(double price, double total, int quantity) {
		 total=total+(price*price);
		return total;
	}
	public double computeSubtotal(double subtotal, double price) {
		subtotal =subtotal+total;
		return subtotal;
	}
	
	// the currency format methods
    public String getPriceFormatted() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String priceFormatted = currency.format(price);
        return priceFormatted;
    }
    
    public String getSubtotalFormatted() {
    	NumberFormat currency = NumberFormat.getCurrencyInstance();
    	String subtotalFormatted = currency.format(subtotal);
    	return subtotalFormatted;
    }
}
