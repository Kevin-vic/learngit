package practice1;
import java.util.Scanner;
public class practice1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("��������ߣ�");
		double height = scanner.nextDouble();
		System.out.println("���������أ�");
		double weight = scanner.nextDouble();
		double bmi = weight / (Math.pow(height, 2));
		System.out.printf("bmi��%.2f\n",bmi);
		
		if (bmi < 18.5) {
			System.out.print("����");
		} else if (18.5 <= bmi && bmi < 25 ) {
			System.out.print("����");
		} else if (25 <= bmi && bmi < 28) {
			System.out.print("����");
		} else {
			System.out.print("�ǳ�����");
		}
	}
}