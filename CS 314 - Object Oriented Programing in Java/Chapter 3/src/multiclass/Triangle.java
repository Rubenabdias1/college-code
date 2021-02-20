package multiclass;

/*
 * Name: Ruben Nunez
 * Assignment: Chapter 4 Exercise 1
 * Description: Triangle class
 */

public class Triangle {
	private double width;
	private double length;
	private double area;
	
	public Triangle() {
		
	}
	
	public void setWidth(double newWidth) {
		width = newWidth;
	}
	
	public double getWidth() {
		return width;
	}
	
	public void setLength(double newLength) {
		length = newLength;
	}
	
	public double getLength() {
		return length;
	}
	
	public double getArea() {
		area = (width * length) / 2;
		return area;
	}

}
