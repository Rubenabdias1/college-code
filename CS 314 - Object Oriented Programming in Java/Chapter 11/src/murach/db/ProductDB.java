package murach.db;

import murach.business.Album;
import murach.business.Book;
import murach.business.Product;
import murach.business.Software;

public class ProductDB {

    public static Product getProduct(String productCode) {
        // In a more realistic application, this code would
        // get the data for the product from a file or database
        // For now, this code just uses if/else statements
        // to return the correct product data

        Product p = null;

        if (productCode.equalsIgnoreCase("java")
                || productCode.equalsIgnoreCase("jsp")
                || productCode.equalsIgnoreCase("mysql")) {
            Book b = new Book();
            if (productCode.equalsIgnoreCase("java")) {
                b.setCode(productCode);
                b.setDescription("Murach's Java Programming");
                b.setPrice(57.50);
                b.setAuthor("Joel Murach");
            } else if (productCode.equalsIgnoreCase("jsp")) {
                b.setCode(productCode);
                b.setDescription("Murach's Java Servlets and JSP");
                b.setPrice(57.50);
                b.setAuthor("Mike Urban");
            } else if (productCode.equalsIgnoreCase("mysql")) {
                b.setCode(productCode);
                b.setDescription("Murach's MySQL");
                b.setPrice(54.50);
                b.setAuthor("Joel Murach");
            }
            p = b; // set Product object equal to the Book object
        } else if (productCode.equalsIgnoreCase("eclipse")) {
            Software s = new Software();
            s.setCode("eclipse");
            s.setDescription("Eclipse");
            s.setPrice(0.00);
            s.setVersion("4.4.2");
            p = s; // set Product object equal to the Software object
        } else if (productCode.equalsIgnoreCase("sgtp")) {
            Album s = new Album();
            s.setCode("sgtp");
            s.setDescription("Sgt. Peppers Lonely Hearts Club Band");
            s.setPrice(14.99);
            s.setArtist("The Beatles");
            p = s; // set Product object equal to the Software object
        } 
        return p;
    }
}
