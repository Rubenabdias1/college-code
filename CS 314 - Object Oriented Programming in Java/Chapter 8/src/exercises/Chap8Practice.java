package exercises;

import java.util.Scanner;
public class Chap8Practice {

	
	
	public static void main(String[] args) {
		
		
		
		System.out.println("Welcome to the grade converter \n");
		
		Scanner sc=new Scanner(System.in);
				String choice="y";
				
				while(choice.equalsIgnoreCase("y")){
					String grade;
					System.out.println("Enter the numerical grade:   ");
					int number=Integer.parseInt(sc.nextLine());
					
					if(number>=90) {
						
						grade="A";
					}
					
					else if (number>=80) {
						grade="B";
										
					}
					
					else if(number >=70) {
						grade="C";
					}
					
					else if (number >=60) {
						
						grade="D";
					
					}
					else {
						grade="F";
					}
				
					System.out.println("The numercial grade is:  \n"+number);
					System.out.println("The grade is:    \n"+grade);
					System.out.println("Do you want to continue (y/n):  \n");
					choice=sc.nextLine();
				}
						System.out.println("Bye");
			sc.close();
	}
}
				
				/*
				while(choice.equalsIgnoreCase("y")){
					String grade;
					System.out.println("Enter the numerical grade:   ");
					
					int number=Integer.parseInt(sc.nextLine());
					
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
				
					System.out.println("The numercial gy"
							+ "The grade is:  \n"+number);
					System.out.println("The grade is:    \n"+grade);
					System.out.println("Do you want to continue (y/n):  \n");
					choice=sc.nextLine();
				}
						System.out.println("Bye");
			sc.close();
	}
}
				
	*/			
				
				
				
				
				/*
				do {
					String grade;
					System.out.println("Enter the numerical grade:   ");
					int number=Integer.parseInt(sc.nextLine());
					
					if(number>=90) {
						
						grade="A";
					}
					
					else if (number>=80) {
						grade="B";
										
					}
					
					else if(number >=70) {
						grade="C";
					}
					
					else if (number >=60) {
						
						grade="D";
					
					}
					else {
						grade="F";
					}
				
					System.out.println("The numercial grade is:  \n"+number);
					System.out.println("The grade is:    \n"+grade);
					System.out.println("Do you want to continue (y/n):  \n");
					choice=sc.nextLine();
				} while(choice.equalsIgnoreCase("y"));
					
					System.out.println("bye");
					sc.close();
					
				}}
				
				*/
				
				
				
				/*
				while(choice.equalsIgnoreCase("y")){
					String grade;
					System.out.println("Enter the numerical grade:   ");
					int number=Integer.parseInt(sc.nextLine());
					
					if(number>=90) {
						
						grade="A";
					}
					
					else if (number>=80) {
						grade="B";
										
					}
					
					else if(number >=70) {
						grade="C";
					}
					
					else if (number >=60) {
						
						grade="D";
					
					}
					else {
						grade="F";
					}
				
					System.out.println("The numercial grade is:  \n"+number);
					System.out.println("The grade is:    \n"+grade);
					System.out.println("Do you want to continue (y/n):  \n");
					choice=sc.nextLine();
				}
						System.out.println("Bye");
			sc.close();
	}
}
	*/
