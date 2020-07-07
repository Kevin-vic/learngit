package practice1;
import java.util.Scanner;
public class practice1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("请输入身高：");
		double height = scanner.nextDouble();
		System.out.println("请输入体重：");
		double weight = scanner.nextDouble();
		double bmi = weight / (Math.pow(height, 2));
		System.out.printf("bmi：%.2f\n",bmi);
		
		if (bmi < 18.5) {
			System.out.print("过轻");
		} else if (18.5 <= bmi && bmi < 25 ) {
			System.out.print("正常");
		} else if (25 <= bmi && bmi < 28) {
			System.out.print("肥胖");
		} else {
			System.out.print("非常肥胖");
		}
	}
}