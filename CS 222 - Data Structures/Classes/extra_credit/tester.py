""" 
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Extra Credit 01
Due Date:		        Friday, Febraury 26, 2021
Date Turned in:         Monday, Febraury 22, 2021
Program Description:    This program tests the Patient class and
                        the Procedure class by creating one instance
                        of the Patient class and three instances of
                        the Procedure class. Then, it prints them out.
                        Finally, it prints out the total charge for
                        all the procedures.

"""

import patient
import procedure
# I'll use datetime module to get the current date 
# as well as formatting methods 

def main ():
    today = "Febraury 22, 2021"

    patientInfo = patient.Patient("Ruben", "Abdias", "Nunez", "15555 10th street","Somewhere", "Missouri", "64030", "(816) 799-5111", "John Locke", "(816) 800-5112")
    physicalExam = procedure.Procedure("Physical Exam", today , "Dr. Irvine", 250.0)
    xRay = procedure.Procedure("X-ray", today, "Dr. Jamison", 500.0)
    bloodTest = procedure.Procedure("Blood Test", today, "Dr. Smith", 200.0)
    


    print(patientInfo, "\n")
    print(physicalExam, "\n")
    print(xRay, "\n")
    print(bloodTest, "\n")

    totalCharges = physicalExam.getCharge() + xRay.getCharge() + bloodTest.getCharge()
    print("Total charge for all tests:", totalCharges)

    
if __name__ == "__main__":
    main()