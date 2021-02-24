package exercises;
import java.text.NumberFormat;

public class StockFirmMethods {

private String stock;
private double price;
private int quantity;
private double total;

    public StockFirmMethods() {
        stock="";
        price=0;
        quantity=0;
        total=0;
    }

    public StockFirmMethods(String stock, double price, int quantity) {
        this.stock=stock;
        this.price=price;
        this.quantity=quantity;
        this.total=quantity*price;
    }

    public void setStock(String stock) {
        this.stock=stock;
    }

    public String getStock() {
        return stock;
    }

    public void setPrice(double price) {
        this.price=price;
    }
    
    public double getPrice() {
        return price;
    }

    public void setQuantity(int quantity) {
        this.quantity=quantity;
    }
    
    public int getQuantity() {
        return quantity;
    }
        
    public double ComputeTotal() {
        total=price*quantity;
        return total;
    }
        
    public String getPriceformatted() {
        NumberFormat currency= NumberFormat.getCurrencyInstance();
        String NumberFormatted= currency.format(price);
        return NumberFormatted;
    }
        
    public String getTotalformatted() {
        NumberFormat currency1=NumberFormat.getCurrencyInstance();
        String NumberFormatted1=currency1.format(total);
        return NumberFormatted1;
    }
             

}