package ui;

import db.StockDB;
import business.Cart;
import business.CartItem;

public class Main {

    public static void main(String args[]) {
        System.out.println("Welcome to the Stock Lister\n");
        
        Cart cart = fillCart();
        System.out.println(cart);
    }
    
    
    
    public static Cart fillCart() {
    	Cart cart = new Cart();
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {
        	// Ask user input
            String stockQuote = Console.getString("Enter Stock code: ");
            int quantity = Console.getInt("Enter the quantity: ");
            
            CartItem stock = StockDB.getStock(stockQuote);
            if (stock == null) {
                System.out.println("The stock code does not match our records.\n");
                continue;
            }
            stock.setQuantity(quantity);
            cart.add(stock);

            // see if the user wants to continue
            choice = Console.getString("Another stock? (y/n): ");
            System.out.println();
        }
        return cart;
    	
    }
    
    
    
    public static void print(Cart cart) {
    	System.out.println(cart);
    }
}