package brubru;

import java.math.BigInteger;

public class Euler20 {
	public static void main(String[] args) {
		BigInteger factorial = factorial(100);
		char[] charArray = factorial.toString().toCharArray();
		BigInteger sum = BigInteger.valueOf(0);
		for (Integer i = 0; i < charArray.length; i++) {
			sum = sum.add(BigInteger.valueOf(Integer.parseInt(((Character) charArray[i]).toString())));
		}
		System.out.println(sum.toString()); // 648
	}
	
	public static BigInteger factorial(Integer n) {
		BigInteger num = BigInteger.valueOf(1);
		for (Integer i = n; i > 0; i--) {
			num = num.multiply(BigInteger.valueOf(i));
		}
		return num;
	}
}
