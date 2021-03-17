package exercises;

public class TravelTimeTrace {

	
	 public static void main(String[] args) {
	        // display a welcome message
	        System.out.println("Welcome to the Travel Time Calculator");
	        System.out.println();  // print a blank line

	     
	      double mph=55;
	      double miles=100;

	            // calculate the travel time in hours with decimal division
	            double hours = miles / mph;

	             System.out.println("This is hours (double) 100/55: \n"+hours+"\n");
	            // get number of minutes as an int
	            int minutes = (int) (hours * 60);
	            System.out.println("This is minutes (int) 60* 1.818 =109.08= 109 :\n"+minutes);

	            // use integer arithmetic to get hours and minutes as int values
	            int hoursInt = minutes / 60;
	            System.out.println("This is hoursInt(int): = 109/60=1 and remainder =49:  \n"+hoursInt);

	            minutes = minutes % 60;
	            System.out.println("This is the minutes(mod) or the remainder: \n"+minutes);


	 }}
	
	
	

