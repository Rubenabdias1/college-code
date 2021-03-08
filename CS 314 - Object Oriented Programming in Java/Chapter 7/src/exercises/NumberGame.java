package exercises;

import java.util.Random;

public class NumberGame {
	private int upperLimit;
	private int number;
	private int guessCount;
	
	public NumberGame() {
		this(50);
	}
	
	public NumberGame(int upperLimit) {
		this.upperLimit = upperLimit = 50;
		Random random = new Random();
		this.number = random.nextInt(upperLimit);
		guessCount = 1;
	}
	
	public int getNumber() {
		return number;
	}
	
	public int getGuessCount() {
		return guessCount;
	}
	
	public int getUpperLimit() {
		return this.upperLimit;
	}
	
	public void incrementGuessCount() {
		guessCount = guessCount + 1;
	}

}
