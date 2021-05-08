package business;

public final class Stock extends CartItem {

	public Stock() {
        super();
    
    }

    public Stock(String quote, String description, double price, int quantity) {
    	super(quote, description, price, quantity); // Instantiating CartItem Class properties
    }
    
    public String getQuote() {
    	return this.getCode();
    }
    
    public void setQuote(String quote) {
    	this.setCode(quote);
    }

}
