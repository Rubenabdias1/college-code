package business;

import java.text.NumberFormat;

public class Cart implements CartConstants {
	private int LENGTH = 100;
	private CartItem[] items;
	private int lastItemIndex; 
	private double total = 0.0;
	
	public Cart() {
		items = new CartItem[LENGTH];
		lastItemIndex = -1;
	}
	
	public boolean add(CartItem item) {
		
		if (lastItemIndex >= LENGTH) {
			System.out.println("The cart is currently full");
			return false;
		}
		
		items[lastItemIndex + 1] = item;
		lastItemIndex++; // Keep track of how many items have been stored
		total += item.getTotal(); // Item's total is added to the cart's total
		return true;
	}

	@Override
	public String toString() {
		StringBuilder list = new StringBuilder();
        list.append(StringUtil.pad("Code", CODE_WIDTH));
        list.append(StringUtil.pad("Description", DESC_WIDTH));
        list.append(StringUtil.pad("Price", PRICE_WIDTH));        
        list.append(StringUtil.pad("Quantity", QUANTITY_WIDTH));      
        list.append("\n");

        list.append(
            StringUtil.pad("=========", CODE_WIDTH));
        list.append(
            StringUtil.pad("=================================", DESC_WIDTH));
        list.append(
            StringUtil.pad("=========", PRICE_WIDTH));     
        list.append(
                    StringUtil.pad("=========", QUANTITY_WIDTH));    
        list.append(
                StringUtil.pad("=========", TOTAL_WIDTH));   
        
        list.append("\n"); 
        if(lastItemIndex > -1) {
            for (int i = 0; i <= lastItemIndex ; i++) {
            	CartItem item = items[i];
            	list.append(
                        StringUtil.pad(item.getCode(), CODE_WIDTH));
                    list.append(
                        StringUtil.pad(item.getDescription(), DESC_WIDTH));
                    list.append(
                        StringUtil.pad(item.getPriceFormatted(), PRICE_WIDTH));
                    list.append(
                            StringUtil.pad(Integer.toString(item.getQuantity()), QUANTITY_WIDTH));
                    list.append(
                            StringUtil.pad(item.getTotalFormatted(), TOTAL_WIDTH));
                    list.append("\n"); 
            }
        	
        }
        int CART_TOTAL_WIDTH = CODE_WIDTH + DESC_WIDTH + PRICE_WIDTH + QUANTITY_WIDTH;
        list.append(
                StringUtil.pad("=========", CART_TOTAL_WIDTH)); 
        list.append("\n"); 
        list.append(
                StringUtil.pad(getTotalFormatted(), CART_TOTAL_WIDTH)); 
        
        return list.toString();
	}
	
    public String getTotalFormatted() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String priceFormatted = currency.format(total);
        return priceFormatted;
    } 

}
