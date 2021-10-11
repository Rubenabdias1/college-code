package exercises;

public class TempTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TempCalculator tc = new TempCalculator();
		
		do {
			tc.output(tc.optionAssign(tc.menu()));
		} while (tc.quit == false);
	}

}
