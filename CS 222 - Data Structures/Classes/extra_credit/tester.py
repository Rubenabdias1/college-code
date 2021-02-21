import patient
import procedure
# I'll use datetime module to get the current date 
# as well as formatting methods
from datetime import datetime 



def main ():
    today = datetime.now()

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