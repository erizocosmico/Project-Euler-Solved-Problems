package brubru;

import java.math.BigInteger;

public class Euler16 {
	public static void main(String[] args) {
		BigInteger number = BigInteger.valueOf(1);
		for (Integer i = 0; i < 1000; i++) {
			number = number.multiply(BigInteger.valueOf(2));
		}
		String numberDigits = number.toString();
		Integer length = numberDigits.length();
		Long digitSum = 0L;
		
		for (Integer i = 0; i < length; i++) {
			Integer digit = Integer.parseInt(numberDigits.substring(i, i+1));
			digitSum += digit;
		}
		
		System.out.println("El resultado es: " + digitSum); // Result: 1366
	}
}
