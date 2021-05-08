package db;

import business.Stock;

public class StockDB implements StockReader {

    public static Stock getStock(String stockCode) {
        Stock s = null;
        
        if (stockCode.equalsIgnoreCase("ko")) {
            s = new Stock();
            s.setQuote(stockCode);
            s.setDescription("Coca Cola stock");
            s.setPrice(57.50);
        } else if (stockCode.equalsIgnoreCase("MSFT")) {
            s = new Stock();
            s.setQuote(stockCode);
            s.setDescription("Microsoft Stock");
            s.setPrice(150.0);
        } else if (stockCode.equalsIgnoreCase("AAPL")) {
            s = new Stock();
            s.setQuote(stockCode);
            s.setDescription("Apple Stock");
            s.setPrice(260.0);
        }

        return s;
    }
}
