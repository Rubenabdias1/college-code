package exercises;

import javax.swing.*;

public class TempCalculator {
	boolean quit = false;
	
	public double input(String value) {
		String ask = "Please Enter " + value;
		
		String input = JOptionPane.showInputDialog(null, ask, "Temperature", JOptionPane.QUESTION_MESSAGE);
		double num = Double.parseDouble(input);
		return num;
	}
	
	public void output(double i) {
		if(i != 0) {
			JOptionPane.showMessageDialog(null,i);
		}
	}
	
	int choice;
	public int menu() {
		String menu = "Welcome to the Temperature Converter!\n";
		menu += "1. Celsius to Fahrenheit\n";
		menu += "2. Fahrenheit to Celsius\n";
		menu += "3. Celsius to Kelvin\n";
		menu += "4. Kelvin to Celsius\n";
		menu += "5. Kelvin to Fahrenheit\n";
		menu += "6. Fahrenheit to Kelvin\n";
		menu += "7. Quit\n\n";
		
		String input = JOptionPane.showInputDialog(null, menu, "Temperature Converter", JOptionPane.QUESTION_MESSAGE);
		
		try {
			choice = Integer.parseInt(input);
		} catch(NumberFormatException e) {
			
		}
		return choice;
		
	}
	
	public double optionAssign(int ch) {
		double output = 0;
		
		switch (ch) {
		case 1: output = CelsiusToFahrenheit(input("Celsius Value")); break;
		case 2: output = FahrenheitToCelsius(input("Fahrenheit Value")); break;
		case 3: output = CelsiusToKelvin(input("Celsius Value")); break;
		case 4: output = KelvinToCelsius(input("Kelvin Value")); break;
		case 5: output = KelvinToFahrenheit(input("Kelvin Value")); break;
		case 6: output = FahrenheitToKelvin(input("Fahrenheit Value")); break;
		case 7: quit(); break;
		default: JOptionPane.showMessageDialog(null, "Invalid Input!"); break;
		}
		
		return output;
	}
	
	public double CelsiusToFahrenheit(double inputC) {
		return (9/5)*inputC + 32;
	}
	
	public double FahrenheitToCelsius(double inputF) {
		return (inputF - 32) * 5/9;
	}
	
	public double CelsiusToKelvin(double inputC) {
		return inputC + 273.15;
	}
	
	public double KelvinToCelsius (double inputk) {
		return inputk - 273.15;
	}
	
	public double KelvinToFahrenheit (double inputK) {
		return inputK * 1.8 - 459.67;
	}
	
	public double FahrenheitToKelvin (double inputF) {
		return 273 + ((inputF - 32.0 ) * (5/9));
	}
	
	public boolean quit() {
		return quit=true;
	}
	

}
