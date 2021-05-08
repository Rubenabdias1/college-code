package db;

import business.Stock;

public interface StockReader {
	static Stock getStock(String quote) {
		return new Stock();
	};
}
