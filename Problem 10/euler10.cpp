//
//  euler10.cpp
//  
//
//  Created by José Miguel Molina Arboledas on 06/05/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
using namespace std;

unsigned int n = 2;
unsigned int primesum = 0;

bool isPrime(int number);

int main(void) {
    while (n < 2000000) {
        if (isPrime(n)) {
            primesum += n;
        }
            n++;
    }
    cout << "The sum of the primes below 2M is " << primesum << endl;
}

bool isPrime(int number) {    
    if (number <= 0 || number == 1 || (number % 2 == 0 && number != 2)) {
        return false;
    } else {
        for (int i = 3; i < number; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
    }
    return true;
}