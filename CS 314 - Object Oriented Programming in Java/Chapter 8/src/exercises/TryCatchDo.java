package exercises;

import java.util.Scanner;
public class TryCatchDo {

	
	
	public static void main(String[] args) {
		
		
		
		System.out.println("Welcome to the grade converter \n");
		
		Scanner sc=new Scanner(System.in);
				String choice="y";
				
				
				do{
					String grade;
					System.out.println("Enter the numerical grade:   ");
					int number;
					try {
					 number=Integer.parseInt(sc.nextLine());
					}
					catch(NumberFormatException e ) {
						System.out.println("Please enter a numerical value\n");
						continue;
										}
					
					switch (number/10) {
				    case 10:
				        grade = "A";
				        break;
				    case 9:
				        grade = "A";
				        break;
				    case 8:
				        grade = "B";
				        break;
				    case 7:
				        grade = "C";
				        break;
				    case 6:
				        grade = "D";
				        break;
				        
				    default:
				        grade = "F";
				        break;
				}
				
					System.out.println("The numercial grade is:  \n"+number);
					System.out.println("The grade is:    \n"+grade);
					System.out.println("Do you want to continue (y/n):  \n");
					choice=sc.nextLine();
				}while(choice.equalsIgnoreCase("y"));
						System.out.println("Bye");
			sc.close();
	}
}
				
				
	