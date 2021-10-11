package business;

import java.text.NumberFormat;

public abstract class CartItem extends Product implements CartConstants {  
	private int quantity = 0;
	private double total = 0;
	
	public CartItem () {
		super();
	}

    public CartItem(String code, String description, double price, int quantity) {
    	super(code, description, price); // Instantiating Product Class properties
    	setQuantity(quantity); // This will also set/calculate the total
    }
	
	@Override
    public void setPrice(double price) {
    	this.price = price;
    	this.total = quantity * price; // auto calculate the total every time the price gets changed
    }
	
	
    public int getQuantity() {
    	return quantity;
    }

    public void setQuantity(int quantity) {
    	this.quantity = quantity;
    	this.total = quantity * this.price; // auto calculate the total every time the quantity gets changed
    }
    
    public double getTotal() {
    	return total;
    }
    
    public String getTotalFormatted() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String priceFormatted = currency.format(total);
        return priceFormatted;
    } 
	
	
	
}
