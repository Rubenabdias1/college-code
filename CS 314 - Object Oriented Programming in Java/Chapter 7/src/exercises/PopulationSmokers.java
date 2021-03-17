package exercises;

import java.util.Scanner;
import java.text.NumberFormat;
import java.math.BigDecimal;
import java.math.RoundingMode;


public class PopulationSmokers {

	public static void main(String[] args) {
		
		double totalsmokers=0;
		double totalcost=0;
		
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in); // create object of the scanner class
		final double population = 35E+4; // declare a constant variable with final access 
		final double TotalhealthCost=33E+3; // declare a constant variable with final access
		 System.out.println("Find the number of smokers in 3 cities \n");
		 for (int i=0; i<3; i++) { // start of the for loop 
			 
			   
		// request input from user
		System.out.println("Please enter the number of smokers in your city:  " );
		int Numsmokers= Integer.parseInt(sc.nextLine());
		System.out.println("Please enter the cost of each smoker in your city:     ");
		double CostofSmoker=Integer.parseInt(sc.nextLine()); 	
	// compound statements 
		totalsmokers+= Numsmokers;	
	 totalcost+= CostofSmoker*Numsmokers;
			
	 
		 } //end for loop
	
		// compute percentage of smokers
		double percentsmokers= (totalsmokers/population);
		// compute percentage cost 
		double percentcost= (totalcost/TotalhealthCost);
		
		 
		
		// round values using BigDecimal class  
	percentsmokers=new BigDecimal(percentsmokers).setScale(2, RoundingMode.HALF_UP).doubleValue();
	percentcost=new BigDecimal(percentcost).setScale(2, RoundingMode.HALF_UP).doubleValue();
	
	// get objects for currency and percent formatting 
	NumberFormat currency= NumberFormat.getCurrencyInstance();
	NumberFormat percent= NumberFormat.getPercentInstance();
	
	//format output
	
	String Message= "The total number of smokers:     "   +totalsmokers+"\n"+
			        "The total cost:                  "  +currency.format(totalcost)+"\n"+
			        "The total percentage of smokers: "+percent.format(percentsmokers)+"\n"+
			        "The total percentage cost:       " +percent.format(percentcost);
	System.out.println(Message);
	
	
	sc.close();
		 
	}
}

	