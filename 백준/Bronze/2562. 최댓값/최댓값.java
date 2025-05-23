import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int ar[] = new int[9];
		int max=ar[0];
		int idx=0;
		for(int i=0;i<ar.length;i++) {
			ar[i]=scan.nextInt();
			if(ar[i]>max) {
				idx=i;
				max=ar[i];
			}
		}
		System.out.println(max);
		System.out.println(idx+1);
	}
}