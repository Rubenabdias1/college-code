package business;

import java.text.NumberFormat;

public abstract class Product {
    private String code;
    private String description;
    protected double price;


    public Product() {
        description = "";
        price = 0;

    }
    
    public void setCode(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }
    
    public Product(String code, String description, double price) {
    	this.code = code;
        this.description = description;
        this.price = price;
    }
    
    public String getDescription() {
    	return description;
    }
    public void setDescription(String description) {
    	this.description = description;
    }
    
    public double getPrice() {
    	return price;
    }
    
    public void setPrice(double price) {
    	this.price = price;
    }
    
    
    public String getPriceFormatted() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String priceFormatted = currency.format(price);
        return priceFormatted;
    }    

}
