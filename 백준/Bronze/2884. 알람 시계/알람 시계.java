import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int hour = scan.nextInt();
		int minute = scan.nextInt();
		
		if((minute-45)<0) {
			if(hour==0) {
				hour=23;
			}else hour--;
			minute = 60+(minute-45);
		}else minute-=45;
		System.out.printf("%d %d",hour,minute);
	}
}