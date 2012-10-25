//
//  Euler12.cpp
//  
//
//  Created by José Miguel Molina Arboledas on 07/05/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

int getDivisorsNumber(unsigned long int n);
unsigned long int getTriangleNumber(int n);

int main() {
    unsigned long int numTriangle = 1;
    unsigned long int number;
    int divisors = 0;
    int maxDivisors = 0;
    
    while (maxDivisors <= 500) {
        number = getTriangleNumber(numTriangle);
        divisors = getDivisorsNumber(number);
        if (divisors > maxDivisors) {
            maxDivisors = divisors;
            if (maxDivisors >= 500) {
                break;
            }
        }
        numTriangle++;
    }
    cout << number << endl; // 76576500
}

int getDivisorsNumber(unsigned long int n) {
    int divisors = 0;
    for (unsigned long long i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            divisors += 2;
        }
    }
    return divisors;
}

unsigned long int getTriangleNumber(int n) {
    unsigned long int num = 0;
    for (int i = 1; i <= n; i++) {
        num += i;
    }
    return num;
}