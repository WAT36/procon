package Atcoder.abc_ontime;

import java.util.Scanner;

public class A_136_Transfer {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		int A =sc.nextInt();
		int B =sc.nextInt();
		int C =sc.nextInt();

		if(C > (A-B)) {
			System.out.println(C-(A-B));
		}else {
			System.out.println(0);
		}
	}

}
